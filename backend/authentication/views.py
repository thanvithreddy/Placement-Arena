from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import LoginSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenRefreshView

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Using a simple approach, just return success
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class AdminUserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        from .models import User
        users = User.objects.all().order_by('-created_at')
        return Response(UserSerializer(users, many=True).data)

    def post(self, request):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        from .models import User
        
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
            role=role
        )
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class AdminUserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        if not request.user.is_admin_user():
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        from .models import User
        
        if request.user.id == id:
            return Response({'error': 'You cannot delete your own account while logged in'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=id)
            user.delete()
            return Response({'message': f'User "{user.username}" deleted successfully'})
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
