from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import LoginSerializer, UserSerializer
from .models import User
from rest_framework_simplejwt.views import TokenRefreshView

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        User.cleanup_expired_pending_users()
        serializer = LoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        User.cleanup_expired_pending_users()
        username = request.data.get('username', '').strip()
        password = request.data.get('password', '').strip()
        email = request.data.get('email', '').strip()
        display_name = request.data.get('display_name', '').strip() or username

        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username__iexact=username).exists():
            return Response({'error': f'User with username "{username}" already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            display_name=display_name,
            role='candidate',
            status='pending'
        )

        return Response({
            'message': 'Sign up request submitted successfully! Your account requires Admin confirmation within 24 hours.',
            'user': UserSerializer(user).data
        }, status=status.HTTP_201_CREATED)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        provided_key = request.META.get('HTTP_X_SESSION_KEY')
        if request.user.session_key and provided_key and provided_key != request.user.session_key:
            return Response({'error': 'duplicate_login', 'message': 'Duplicate login detected from another device/session.'}, status=status.HTTP_409_CONFLICT)

        serializer = UserSerializer(request.user)
        data = serializer.data
        from .models import DailyStreak
        streak_obj = DailyStreak.objects.filter(user=request.user).first()
        data['current_streak'] = streak_obj.current_streak if streak_obj else 0
        data['longest_streak'] = streak_obj.longest_streak if streak_obj else 0
        data['last_exam_date'] = str(streak_obj.last_exam_date) if streak_obj and streak_obj.last_exam_date else None
        return Response(data)

class StreakView(APIView):
    """GET /api/auth/streak/ — Returns the current user's daily exam streak."""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        from .models import DailyStreak
        from datetime import date
        streak_obj, _ = DailyStreak.objects.get_or_create(user=request.user)
        today = date.today()
        is_active_today = streak_obj.last_exam_date == today
        return Response({
            'current_streak': streak_obj.current_streak,
            'longest_streak': streak_obj.longest_streak,
            'last_exam_date': str(streak_obj.last_exam_date) if streak_obj.last_exam_date else None,
            'is_active_today': is_active_today,
        })

class AdminUserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        User.cleanup_expired_pending_users()
        users = User.objects.all().order_by('-created_at')
        return Response(UserSerializer(users, many=True).data)

    def post(self, request):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)

        username = request.data.get('username', '').strip()
        password = request.data.get('password', '').strip()
        display_name = request.data.get('display_name', '').strip() or username
        role = request.data.get('role', 'candidate')
        email = request.data.get('email', '').strip()

        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username__iexact=username).exists():
            return Response({'error': f'User with username "{username}" already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            display_name=display_name,
            role=role,
            status='confirmed'
        )
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

class AdminConfirmUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = User.objects.get(id=id)
            user.status = 'confirmed'
            user.save()
            return Response({'message': f'User "{user.username}" has been confirmed successfully.', 'user': UserSerializer(user).data})
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

class AdminUserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)

        if request.user.id == id:
            return Response({'error': 'You cannot delete your own account while logged in'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=id)
            user.delete()
            return Response({'message': f'User "{user.username}" deleted successfully'})
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
