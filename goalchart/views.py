from django.shortcuts import render, get_object_or_404, redirect
from goalchart.models import Student, Schedule, Goals
from django.contrib.auth.decorators import login_required

@login_required
def goal_per_day(request, id):
    student = get_object_or_404(Student, id=id)
    context = {
        "student": student,
    }
    return render(request, "goal_chart.html", context)

@login_required
def goal_list(request):
    students = Student.objects.all()
    context = {
        "students": students,
    }
    return render(request, "goalchart/teacher_home.html", context)

@login_required
def average_rating(request):
    rating = goal_ratings.get(Goals, id=id)
    ratings = goal.goal_ratings.all()

    avg_rating = ratings/len(ratings)
