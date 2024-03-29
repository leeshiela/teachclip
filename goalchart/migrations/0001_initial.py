# Generated by Django 5.0 on 2023-12-10 04:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_name', models.CharField(max_length=200)),
                ('goal_description', models.TextField()),
                ('goal_picture', models.URLField()),
            ],
            options={
                'ordering': ['goal_name'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_first_name', models.CharField(max_length=200)),
                ('year_in_school', models.CharField(choices=[('K', 'Kindergarten'), ('G1', '1st Grade'), ('G2', '2nd Grade'), ('G3', '3rd Grade'), ('G4', '4th Grade'), ('G5', '5th Grade'), ('GO', 'Other')], default='K', max_length=2)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['student_first_name'],
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_the_week', models.CharField(choices=[('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THU', 'Thursday'), ('FRI', 'Friday')], default='MON', max_length=3)),
                ('period_number', models.PositiveSmallIntegerField(default=1)),
                ('activity', models.CharField(max_length=200)),
                ('picture', models.URLField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='goalchart.student')),
            ],
            options={
                'ordering': ['activity'],
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(default=0)),
                ('goals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goal_ratings', to='goalchart.goals')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='goalchart.student')),
            ],
        ),
        migrations.AddField(
            model_name='goals',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='goalchart.student'),
        ),
    ]
