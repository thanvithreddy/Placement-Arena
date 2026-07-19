from rest_framework import serializers
from .models import Question, Option, Answer

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text', 'order'] # Exclude is_correct for candidates

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['id', 'text', 'explanation', 'marks', 'category', 'difficulty', 'order', 'options']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question_id', 'selected_option_id', 'is_correct', 'marks_awarded']

# Admin serializers
class AdminOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class AdminQuestionSerializer(serializers.ModelSerializer):
    options = AdminOptionSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = '__all__'
