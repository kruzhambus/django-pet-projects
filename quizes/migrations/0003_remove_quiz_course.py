# Generated by Django 3.2.5 on 2021-10-10 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0002_quiz_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='course',
        ),
    ]
