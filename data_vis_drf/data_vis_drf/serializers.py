from rest_framework import serializers
from .models import AccountUser, QuestionnaireQuestion, QuestionnaireUseranswer

class AccountUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'location', 'profile_image', 'description', 'name', 'university', 'is_organization_admin', 'email_verified')

class QuestionnaireQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireQuestion
        fields = ('id', 'text', 'answer_type', 'order', 'reverse_scored', 'category', 'label', 'state', 'created_by', 'is_delete')

class QuestionnaireUseranswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireUseranswer
        fields = ['text_answer', 'slider_answer', 'numeric_answer', 'timestamp', 'choice_answer', 'question', 'user', 'reactions_ms', 'question_group']
