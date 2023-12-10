from django.shortcuts import render, get_object_or_404, redirect
from goalchart.models import Student, Schedule, Goals, Rating
from django.contrib.auth.decorators import login_required

def goal_per_day(request, id):
    goals = get_object_or_404(Goals, id=id)
    schedule = get_object_or_404(Schedule, id=id)
    context = {
        "goals": goals,
        "schedule": schedule,
    }
    return render(request, "goal_chart.html", context)

def goal_list(request, id):
    list_of_goals = get_object_or_404(Goals, id=id)
    students = Student.objects.all()
    context = {
        "students": students,
        "goals": list_of_goals,
    }
    return render(request, "teacher_home.html", context)
