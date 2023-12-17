from django.urls import path
from accounts.views import teacher_login, user_logout, create_teacher_user

urlpatterns = [
    path("teacher_login/", teacher_login, name="teacher_login"),
    path("logout/", user_logout, name="logout"),
    path("teacher_signup/", create_teacher_user, name="teacher_signup"),
]
