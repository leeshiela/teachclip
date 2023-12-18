from django.contrib import admin
from .models import Student, Schedule, Goal

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "student_first_name",
        "grade_in_school",
        "created_on",
        "last_modified",

    ]

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "student",
        "day_of_the_week",
        "period_number",
        "activity",
        "picture",

    ]

@admin.register(Goal)
class GoalsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "student",
        "schedule",
        "goal_name",
        "goal_description",
        "goal_picture",
        "goal_rating",

    ]

# @admin.register(Rating)
# class RatingAdmin(admin.ModelAdmin):
#     list_display = [
#         "id",
#         "goals",
#         "rating",
#     ]
