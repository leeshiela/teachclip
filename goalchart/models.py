from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.conf import settings

class Student(models.Model):
    student_first_name = models.CharField(max_length=200)

    GRADE_IN_SCHOOL_CHOICES = [
        ("K", "Kindergarten"),
        ("G1", "1st Grade"),
        ("G2", "2nd Grade"),
        ("G3", "3rd Grade"),
        ("G4", "4th Grade"),
        ("G5", "5th Grade"),
        ("GO", "Other"),
    ]

    grade_in_school = models.CharField(
        max_length=2,
        choices=GRADE_IN_SCHOOL_CHOICES,
        default="K",
    )
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_first_name

    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="students",
        on_delete=models.CASCADE,
        null=True,
    )
    # parent = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     related_name = "students",
    #     on_delete = models.CASCADE,
    #     null=True
    # )
    class Meta:
        ordering = ["student_first_name"]
    # Add Parent Foreign Key

class Activity(models.Model):
    activity_name = models.CharField(max_length=200, null=True)
    activity_description = models.TextField(null=True)
    activity_picture_url = models.URLField(null=True)

    def __str__(self):
        return self.activity_name

    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="activities",
        on_delete=models.CASCADE,
        null=True,
    )

class Schedule(models.Model):
    student = models.ForeignKey(
        Student,
        related_name="schedules",
        on_delete=models.CASCADE,
        null=True,
    )
    date = models.DateField(null=True)
    # MONDAY = "MON"
    # TUESDAY = "TUE"
    # WEDNESDAY = "WED"
    # THURSDAY = "THU"
    # FRIDAY = "FRI"

    # DAY_OF_WEEK = {
    #     MONDAY: "Monday",
    #     TUESDAY: "Tuesday",
    #     WEDNESDAY: "Wednesday",
    #     THURSDAY: "Thursday",
    #     FRIDAY: "Friday",
    # }

    # day_of_the_week = models.CharField(
    #     max_length=3,
    #     choices=DAY_OF_WEEK,
    #     default=MONDAY,
    # )
    def __str__(self):
        return self.date.strftime('%A %b %d %Y')

    activity_1 = models.ForeignKey(
        Activity,
        related_name="schedule_activity_1",
        on_delete=models.CASCADE,
        null=True,
    )


    activity_2 = models.ForeignKey(
        Activity,
        related_name="schedule_activity_2",
        on_delete=models.CASCADE,
        null=True,
    )


    activity_3 = models.ForeignKey(
        Activity,
        related_name="schedule_activity_3",
        on_delete=models.CASCADE,
        null=True,
    )


    activity_4 = models.ForeignKey(
        Activity,
        related_name="schedule_activity_4",
        on_delete=models.CASCADE,
        null=True,
    )

    activity_5 = models.ForeignKey(
        Activity,
        related_name="schedule_activity_5",
        on_delete=models.CASCADE,
        null=True,
    )


    activity_6 = models.ForeignKey(
        Activity,
        related_name="schedule_activity_6",
        on_delete=models.CASCADE,
        null=True,
    )


    activity_7 = models.ForeignKey(
        Activity,
        related_name="schedule_activity_7",
        on_delete=models.CASCADE,
        null=True,
    )

    # class Meta:
    #     ordering = ["activity"]


class Goal(models.Model):
    student = models.ForeignKey(
        Student,
        related_name="goals",
        on_delete=models.CASCADE,
        null=True,
    )
    schedule = models.ForeignKey(
        Schedule,
        related_name="goals",
        on_delete=models.CASCADE,
        null=True,
    )
    goal_name = models.CharField(max_length=200)
    goal_description = models.TextField()
    goal_picture = models.URLField()
    last_modified = models.DateTimeField(auto_now=True, null=True)
    goal_rating = models.PositiveSmallIntegerField(default = 0,null=True)

    # def __str__(self):
    #     return self.goal_name

    def average_rating(self) -> float:
        return Rating.objects.filter(goals=self).aggregate(Avg("rating")) ["rating_avg"] or 0

    def __str__(self):
        return f"{self.goal_name}: {self.average_rating()}"

    class Meta:
        ordering = ["goal_name"]


class Rating(models.Model):
    goals = models.ForeignKey(
        Goal,
        related_name="goal_ratings",
        on_delete=models.CASCADE,
        null=True,
    )

    rating = models.PositiveSmallIntegerField(default = 0)

    def __str__(self):
        return f"{self.goals.goal_name}: {self.rating}"
