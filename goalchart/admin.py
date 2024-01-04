from django.contrib import admin
from .models import Student, Schedule, Goal, Activity

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
        "date",
        "activity_1",
        "activity_2",
        "activity_3",
        "activity_4",
        "activity_5",
        "activity_6",
        "activity_7",
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

@admin.register(Activity)
class Activity(admin.ModelAdmin):
    list_display = [
        "id",
        "activity_name",
        "activity_description",
        "activity_picture_url",
    ]
