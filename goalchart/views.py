from django.shortcuts import render, get_object_or_404, redirect
from goalchart.models import Student, Activity, Schedule, Goal, Rating
from django.contrib.auth.decorators import login_required
from goalchart.forms import CreateStudentGoal, AddStudent, AddActivity, CreateSchedule
from django.http import HttpResponse, HttpRequest

@login_required
def goal_per_day(request, id):
    goal = get_object_or_404(Goal, id=id)
    context = {
        "goal": goal,
    }
    return render(request, "goalchart/goal_chart.html", context)

@login_required
def add_activity(request):
    if request.method == "POST":
        form = AddActivity(request.POST)
        if form.is_valid():
            activity = form.save(False)
            activity.teacher = request.user
            activity.save()
            return redirect("schedules")
    else:
        form = AddActivity()
    context = {
        "activity_form": form,
    }
    return render(request, "goalchart/add_activity.html", context)


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
def create_student_goal(request, id):
    if request.method == "POST":
        form = CreateStudentGoal(request.POST)
        if form.is_valid():
            goal = form.save(False)
            goal.student = Student.objects.get(id=id)
            goal.teacher = request.user
            goal.save()
            return redirect("teacher_home")
    else:
        form = CreateStudentGoal()
    context = {
        "goal_form": form,
        "student_name": Student.objects.get(id=id).student_first_name
    }
    return render(request, "goalchart/create_goal.html", context)

@login_required
def edit_student_goal(request, id):
    goal = get_object_or_404(Goal, id=id)
    if request.method == "POST":
        form = CreateStudentGoal(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect("teacher_home")
    else:
        form = CreateStudentGoal(instance=goal)
    context = {
        "goal": goal,
        "edit_goal": form,
    }
    return render(request, "goalchart/edit_goal.html", context)


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

@login_required
def create_student_schedule_calendar(request):
    if request.method == "POST":
        form = CreateSchedule(request.POST)
        if form.is_valid():
            schedule = form.save(False)
            schedule.teacher = request.user
            schedule.save()
            return redirect("teacher_home")
    else:
        form = CreateSchedule()
    context = {
        "schedule_form": form,
    }
    return render(request, "goalchart/student_calendar.html", context)

def index(request: HttpRequest) -> HttpResponse:
    goals = Goal.objects.all()
    for goal in goals:
        rating = Rating.objects.filter(goal=goal, user=request.user).first()
        goal.user_rating = rating.rating if rating else 0
    return render(request, "goalchart/goal_chart.html", {"goals": goals})

def rate(request: HttpRequest, goal_id: int, rating: int) -> HttpResponse:
    goal = Goal.objects.get(id=goal_id)
    Rating.objects.filter(goal=goal, user=request.user).delete()
    Goal.rating_set.create(user=request.user, rating=rating)
    return index(request, "goalchart/teacher_home.html")
