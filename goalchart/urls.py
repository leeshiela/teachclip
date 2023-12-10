from django.urls import path
from goalchart.views import goal_per_day, goal_list

urlpatterns = [
    path("<int:id>/", goal_per_day, name="goal_chart"),
    path("teacher_home/", goal_list, name="teacher_home"),
]
