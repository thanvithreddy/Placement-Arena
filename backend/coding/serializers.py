from rest_framework import serializers
from .models import CodingProblem, SampleTestCase, HiddenTestCase, CodingSubmission

class SampleTestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleTestCase
        fields = '__all__'

class HiddenTestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HiddenTestCase
        fields = '__all__'

class CodingProblemSerializer(serializers.ModelSerializer):
    sample_cases = SampleTestCaseSerializer(many=True, read_only=True)
    class Meta:
        model = CodingProblem
        fields = '__all__'

class CodingSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodingSubmission
        fields = '__all__'

# Admin Serializers
class AdminCodingProblemSerializer(serializers.ModelSerializer):
    sample_cases = SampleTestCaseSerializer(many=True, read_only=True)
    hidden_cases = HiddenTestCaseSerializer(many=True, read_only=True)
    class Meta:
        model = CodingProblem
        fields = '__all__'
