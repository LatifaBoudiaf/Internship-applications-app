# Generated by Django 4.2 on 2023-04-29 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('companyID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('companyName', models.CharField(max_length=200)),
                ('companyAddress', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='internshipOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicationDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('duration', models.IntegerField()),
                ('subject', models.CharField(max_length=200)),
                ('offeredBy', models.CharField(max_length=200)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('details', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('univName', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('univAddress', models.CharField(max_length=255)),
                ('univDirectorName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('facultyID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('facultyName', models.CharField(max_length=200)),
                ('univName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.university')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('depID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('depName', models.CharField(max_length=200)),
                ('facultyID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.faculty')),
            ],
        ),
    ]
