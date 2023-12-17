from django.urls import path
from goalchart.views import goal_per_day, goal_list
from django.views.generic.base import TemplateView


urlpatterns = [
    path("<int:id>/", goal_per_day, name="goal_chart"),
    path("teacher_home/", goal_list, name="teacher_home"),
    path("info/", TemplateView.as_view(template_name="goalchart/info.html"), name="info"),
    path("profile_selection/", TemplateView.as_view(template_name="goalchart/profile_selection.html"), name="profile_selection"),
    path("about/", TemplateView.as_view(template_name="goalchart/about.html"), name="about"),
]
