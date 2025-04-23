from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Jobs(models.Model):

    ALL_JOB_TYPES = [
        ('FT', 'Full-time'),
        ('PT', 'Part-time'),
        ('CT', 'Contract'),
        ('IN', 'Internship'),
    ]

    job_name = models.CharField(max_length=100)
    job_description = models.TextField()
    job_location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=2, choices=ALL_JOB_TYPES)  # e.g., Full-time, Part-time, Contract, Internship
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_posted = models.DateTimeField(default=timezone.now)
    company_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.job_name


class JobApplication(models.Model):
    full_name = models.CharField(max_length=255)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    email = models.EmailField()
    salary_expectation = models.DecimalField(max_digits=10, decimal_places=2)
    about = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.FileField(upload_to='cover_letters/')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.job.job_name}"
