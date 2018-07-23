from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'questions'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/login'}, name='logout'),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('change_password/', views.change_password, name='change_password'),
    path('skills/<int:pk>/', views.SkillView.as_view(), name="skill"),
    path('questions/<int:pk>/', views.QuestionView.as_view(), name="question"),
    path('random/', views.get_random_question, name='random'),
    path('ajax/send_code/', views.send_code, name="send_code"),
    path('ajax/get_output/', views.get_output, name="get_output"),
]