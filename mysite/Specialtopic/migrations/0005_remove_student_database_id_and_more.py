# Generated by Django 4.1.1 on 2022-10-03 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Specialtopic', '0004_student_database_id_alter_student_database_usn_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_database',
            name='id',
        ),
        migrations.AlterField(
            model_name='student_database',
            name='USN',
            field=models.CharField(max_length=11, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='system_database',
            name='USN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Specialtopic.student_database'),
        ),
    ]