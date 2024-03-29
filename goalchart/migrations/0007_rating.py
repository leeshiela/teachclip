# Generated by Django 5.0 on 2023-12-17 17:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goalchart', '0006_alter_goals_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(default=0)),
                ('goals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goal_ratings', to='goalchart.goals')),
            ],
        ),
    ]
