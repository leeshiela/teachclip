from django import forms
from goalchart.models import Student, Schedule, Goal, Rating

# Create a goal for a student
class CreateStudentGoal(forms.ModelForm):
    class Meta:
        model = Goal
        fields = [
            "student",
            "schedule",
            "goal_name",
            "goal_description",
            "goal_picture",
            "goal_rating",
        ]

class AddStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "student_first_name",
            "grade_in_school",
        ]
