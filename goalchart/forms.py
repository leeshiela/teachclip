from django import forms
from django.forms import DateInput
from goalchart.models import Student, Activity, Schedule, Goal, Rating

# Create a goal for a student
class CreateStudentGoal(forms.ModelForm):
    class Meta:
        model = Goal
        fields = [
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

class AddActivity(forms.ModelForm):
    class Meta:
        model = Activity
        fields = [
            "activity_name",
            "activity_description",
            "activity_picture_url",
        ]

class CalendarInput(DateInput):
    input_type = "date"

class CreateSchedule(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     self.user_id = kwargs.pop("user")
    #     self.user = Student.objects.get(id=self.user_id)
    #     super(CreateStudentGoal, self).__init__(*args, **kwargs)
    #     # self.fields["student"].queryset = Student.objects.filter(
    #     #     student=self.user
    #     # )
    #     self.fields["schedule"].queryset = Schedule.objects.filter(
    #         student=self.user
    #     )
    class Meta:
        model = Schedule
        fields = [
            "date",
            "activity_1",
            "activity_2",
            "activity_3",
            "activity_4",
            "activity_5",
            "activity_6",
            "activity_7",
        ]
        widgets = {"date": CalendarInput(format=("%A %b %d %Y"))}
