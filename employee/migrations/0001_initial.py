# Generated by Django 3.2.5 on 2021-07-27 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateLeaveInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leavefrom', models.DateField()),
                ('leavetill', models.DateField()),
                ('leavetype', models.CharField(max_length=50)),
                ('leavedesc', models.TextField()),
            ],
        ),
    ]
