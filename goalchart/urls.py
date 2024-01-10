from django.urls import path
from goalchart.views import goal_per_day, goal_list, add_student, create_student_goal, edit_student_goal, add_activity, create_student_schedule_calendar, index, rate
from django.views.generic.base import TemplateView


urlpatterns = [
    path("<int:id>/", goal_per_day, name="goal_chart"),
    path("teacher_home/", goal_list, name="teacher_home"),
    path("info/", TemplateView.as_view(template_name="goalchart/info.html"), name="info"),
    path("profile_selection/", TemplateView.as_view(template_name="goalchart/profile_selection.html"), name="profile_selection"),
    path("about/", TemplateView.as_view(template_name="goalchart/about.html"), name="about"),
    path("add_student/", add_student, name="add_student"),
    path("create_goal/<int:id>/", create_student_goal, name="create_goal"),
    path("edit_goal/<int:id>/", edit_student_goal, name="edit_goal"),
    path("add_activity/", add_activity, name="add_activity"),
    path("schedules/", create_student_schedule_calendar, name="schedules"),
]
