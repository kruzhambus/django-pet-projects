from django.urls import path
from .views import (
    QuizListView,
    quiz_view,
    quiz_data_view,
    save_quiz_view,
    login_action,
    Search
)

app_name = 'quizes'

urlpatterns = [
    path("search/", Search.as_view(), name='search'),
    path('', QuizListView.as_view(), name='main-view'),
    path('<pk>/', login_action, name='quiz-view'),
    path('<pk>/save/', save_quiz_view, name='save-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),

]