from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

class Student(models.Model):
    student_first_name = models.CharField(max_length=200)
    KINDERGARTEN = "K"
    FIRST = "G1"
    SECOND = "G2"
    THIRD = "G3"
    FOURTH = "G4"
    FIFTH = "G5"
    OTHER = "GO"
    YEAR_IN_SCHOOL_CHOICES = {
        KINDERGARTEN: "Kindergarten",
        FIRST: "1st Grade",
        SECOND: "2nd Grade",
        THIRD: "3rd Grade",
        FOURTH: "4th Grade",
        FIFTH: "5th Grade",
        OTHER: "Other",
    }

    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=KINDERGARTEN,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_first_name
    class Meta:
        ordering = ["student_first_name"]
    # Add Teacher Foreign Key
    # Add Parent Foreign Key


class Schedule(models.Model):
    student = models.ForeignKey(
        Student,
        related_name="schedule",
        on_delete=models.CASCADE,
    )
    MONDAY = "MON"
    TUESDAY = "TUE"
    WEDNESDAY = "WED"
    THURSDAY = "THU"
    FRIDAY = "FRI"

    DAY_OF_WEEK = {
        MONDAY: "Monday",
        TUESDAY: "Tuesday",
        WEDNESDAY: "Wednesday",
        THURSDAY: "Thursday",
        FRIDAY: "Friday",
    }

    day_of_the_week = models.CharField(
        max_length=3,
        choices=DAY_OF_WEEK,
        default=MONDAY,
    )

    period_number = models.PositiveSmallIntegerField(default=1)
    activity = models.CharField(max_length=200)
    picture = models.URLField()

    class Meta:
        ordering = ["activity"]


class Goals(models.Model):
    student = models.ForeignKey(
        Student,
        related_name="goals",
        on_delete=models.CASCADE,
    )
    goal_name = models.CharField(max_length=200)
    goal_description = models.TextField()
    goal_picture = models.URLField()

    def average_rating(self) -> float:
        return Rating.objects.filter(goals=self).aggregate(Avg("rating")) ["rating_avg"]

    def __str__(self):
        return f"{self.goal_name}: {self.average_rating()}"

    class Meta:
        ordering = ["goal_name"]


class Rating(models.Model):
    student = models.ForeignKey(
        Student,
        related_name="ratings",
        on_delete=models.CASCADE,
    )
    goals = models.ForeignKey(
        Goals,
        related_name="goal_ratings",
        on_delete=models.CASCADE
    )
    rating = models.PositiveSmallIntegerField(default = 0)

    def __str__(self):
        return f"{self.goals.goal_name}: {self.rating}"
