from django.shortcuts import render, get_object_or_404, redirect
from goalchart.models import Student, Schedule, Goal, Rating
from django.contrib.auth.decorators import login_required
from goalchart.forms import CreateStudentGoal, AddStudent

@login_required
def goal_per_day(request, id):
    student = get_object_or_404(Student, id=id)
    context = {
        "student": student,
    }
    return render(request, "goalchart/goal_chart.html", context)

@login_required
def goal_list(request):
    students = Student.objects.filter(teacher=request.user)
    context = {
        "students": students,
    }
    return render(request, "goalchart/teacher_home.html", context)

@login_required
def average_rating(request):
    rating = get_object_or_404(Goal, id=id)
    ratings = Rating.objects.all()

    avg_rating = ratings/len(ratings)

@login_required
def create_student_goal(request):
    if request.method == "POST":
        form = CreateStudentGoal(request.POST)
        if form.is_valid():
            goal = form.save(False)
            goal.teacher = request.user
            goal.save()
            return redirect("teacher_home")
    else:
        form = CreateStudentGoal()
    context = {
        "goal_form": form,
    }
    return render(request, "goalchart/create_goal.html", context)

@login_required
def add_student(request):
    if request.method == "POST":
        form = AddStudent(request.POST)
        if form.is_valid():
            new_student = form.save(False)
            new_student.teacher = request.user
            new_student.save()
            return redirect("teacher_home")
    else:
        form = AddStudent()
    context = {
        "student_form": form,
    }
    return render(request, "goalchart/add_student.html", context)
