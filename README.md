# TeachClip by Shiela Lee

TeachClip is a web application that allows teachers and students to create goals for students. This was born out of my experience as a teacher and I noticed students needed to keep track of their goals. Many of the special needs students needed to bring their paper goal charts to their classes and it was becoming cumbersome to bring so many papers and to fill out whether or not they met the goal or not. TeachClip makes the goal tracking easier. Create your own students and create goals for them. Set the daily schedule by creating activities and then putting those activities into a schedule. Then create the goal.

## Getting started
This project is entirely run on python and Django.

1. Start by forking this repository.

2. Clone the forked repository onto your local computer:
git clone <https://github.com/leeshiela/teachclip>

3. Start the project by running this command:

```
python manage.py runserver
```

4. View the project in the browser: http://localhost:8000/

![Creating Students image](/resources/my-students.png)
![Creating a Schedule image](/resources/schedule.png)
![Creating a goal chart image](/resources/goal-chart.png)


## How It Works

1. Once you have it up and running, create a teacher account by clicking "Sign Up"
2. Then, create some students.
3. On the navigation bar, click "Create a Schedule"
4. Add at least 7 activities for the day
5. Once you've added those 7 activities, return to "Create a Schedule" and click on a day you want to create a schedule for. Then, from the dropdown  menu, you should see all your activities. Input 7 activities into the schedule.
6. Return to your "My Students" page and create some students and add goals for them by clicking on the "+Goal" link in each student box.
7. When you click on the stars, you should see the goal chart populate!

## Future Development

Future features:
- Clickable log of star ratings
- Average star rating over time
- Notification for when the star ratings reach a threshold. Notifies teacher that the student is either failing to meet or is already meeting their goal
