# Generated by Django 5.0 on 2023-12-11 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goalchart', '0003_goals_last_modified_alter_schedule_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='student',
        ),
    ]