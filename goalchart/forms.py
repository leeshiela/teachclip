from django import forms
from django.forms import DateInput
from goalchart.models import Student, Schedule, Goal, Rating

class CalendarInput(DateInput):
    input_type = "datetime-local"

# Create a goal for a student
class CreateStudentGoal(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        print("before")
        self.user_id = kwargs.pop("user")
        print("after")
        self.user = Student.objects.get(id=self.user_id)
        super(CreateStudentGoal, self).__init__(*args, **kwargs)
        # self.fields["student"].queryset = Student.objects.filter(
        #     student=self.user
        # )
        self.fields["schedule"].queryset = Schedule.objects.filter(
            student=self.user
        )

    class Meta:
        model = Goal
        fields = [
            "schedule",
            "goal_name",
            "goal_description",
            "goal_picture",
            "goal_rating",
        ]
        widgets = {"schedule": CalendarInput(format="%Y-%m-%dT%H:%M")}



class AddStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "student_first_name",
            "grade_in_school",
        ]
