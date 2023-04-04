from django.urls import path

from . import views

urlpatterns = [
    path('user_list/', views.user_list, name='user_list'),
    path('user_list/<int:user_id>/', views.user_list, name='user_list_with_id'),
    path('questionnaire_user_answers/<int:question_id>/<int:user_id>/', views.questionnaire_user_answers, name='questionnaire_user_answers'),
    path('question_text/<int:question_id>/', views.question_text, name='question_text'),
]