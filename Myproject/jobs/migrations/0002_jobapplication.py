# Generated by Django 5.2 on 2025-04-23 06:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('salary_expectation', models.DecimalField(decimal_places=2, max_digits=10)),
                ('about', models.TextField()),
                ('resume', models.FileField(upload_to='resumes/')),
                ('cover_letter', models.FileField(upload_to='cover_letters/')),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobs')),
            ],
        ),
    ]
