# Generated by Django 4.1.1 on 2022-09-14 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=50)),
                ('USN', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='System_database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=50)),
                ('Branch', models.CharField(max_length=10)),
                ('USN', models.CharField(max_length=11)),
                ('System_no', models.CharField(max_length=9)),
                ('Time_in', models.TimeField()),
                ('Time_out', models.TimeField()),
            ],
        ),
    ]