from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import AccountUser
from django.db import connection

# http://127.0.0.1:8000/user_list/72/
@api_view(['GET'])
def user_list(request, user_id=None):
    with connection.cursor() as cursor:
        if user_id:
            cursor.execute("SELECT username, email FROM account_user WHERE id = %d" % (user_id))
        else:
            cursor.execute("SELECT username, email FROM account_user")
        rows = cursor.fetchall()
    return Response(rows)

# http://127.0.0.1:8000/question_text/36/
@api_view(['GET'])
def question_text(request, question_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT text FROM questionnaire_question WHERE id = %d" % (question_id))
        rows = cursor.fetchall()
    return Response(rows)

# http://127.0.0.1:8000/questionnaire_user_answers/36/72/
@api_view(['GET'])
def questionnaire_user_answers(request, question_id, user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT timestamp, text_answer, slider_answer, numeric_answer FROM questionnaire_useranswer \
            WHERE question_id = %d AND user_id = %d" % (question_id, user_id))
        rows = cursor.fetchall()
    return Response(rows)