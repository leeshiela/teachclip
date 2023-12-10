from django.contrib import admin
from .models import Student, Schedule, Goals, Rating

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

@admin.register(Goals)
class GoalsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "student",
        "goal_name",
        "goal_description",
        "goal_picture",
        "average_rating",

    ]

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "student",
        "goals",
        "rating",
    ]
