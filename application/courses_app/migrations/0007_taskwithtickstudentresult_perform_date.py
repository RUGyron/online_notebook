# Generated by Django 2.2.6 on 2020-06-23 13:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0006_section_taskwithtick_taskwithtickoption_taskwithtickstudentresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskwithtickstudentresult',
            name='perform_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
