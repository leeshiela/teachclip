# Generated by Django 5.0 on 2023-12-17 23:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goalchart', '0008_remove_goals_student_goals_schedule_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='goals',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='goalchart.student'),
        ),
    ]
