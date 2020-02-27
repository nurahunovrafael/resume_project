from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    about = models.TextField(max_length=500)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)

class Education(models.Model):
    school = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    DEGREE_CHOICES = (('elementary_education', 'Elementary education'),
    ('secondary education', 'Secondary education'), ('vocational education', 'Vocational education'),
    ('bachelor degree', 'Bachelor degree'), ('specialist degree', 'Specialist degree'), 
    ('magister degree', 'Magister degree'),)
    degree = models.CharField(max_length=100, choices=DEGREE_CHOICES )
    Resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    
class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    Resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

