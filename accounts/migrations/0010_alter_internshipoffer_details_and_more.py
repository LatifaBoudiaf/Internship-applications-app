# Generated by Django 4.2 on 2023-05-13 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_student_applications_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internshipoffer',
            name='details',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='internshipoffer',
            name='offeredBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.company'),
        ),
    ]
