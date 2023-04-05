from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import AccountUser, QuestionnaireQuestion, QuestionnaireUseranswer
from django.db import connection
from .serializers import AccountUserSerializer, QuestionnaireQuestionSerializer, QuestionnaireUseranswerSerializer
from django.db.models import Q

# http://127.0.0.1:8000/user_list/72/
@api_view(['GET'])
def user_list(request, user_id=None):
    if user_id:
        users = AccountUser.objects.filter(id=user_id)
    else:
        users = AccountUser.objects.all()
    serializer = AccountUserSerializer(users, many=True)
    return Response(serializer.data)

# http://127.0.0.1:8000/question_text/36/
@api_view(['GET'])
def question_text(request, question_id):
    question = QuestionnaireQuestion.objects.get(id=question_id)
    serializer = QuestionnaireQuestionSerializer(question)
    return Response(serializer.data)

# http://127.0.0.1:8000/questionnaire_user_answers/36/72/
@api_view(['GET'])
def questionnaire_user_answers(request, question_id, user_id):
    user_answers = QuestionnaireUseranswer.objects.filter(
        Q(question=question_id) &
        Q(user=user_id) &
        (Q(text_answer__isnull=False) | Q(slider_answer__isnull=False) | Q(numeric_answer__isnull=False))
    )
    serializer = QuestionnaireUseranswerSerializer(user_answers, many=True)
    return Response(serializer.data)
