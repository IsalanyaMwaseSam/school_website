from django.db import models
from education.choices import *

class Course(models.Model):
  course = models.CharField(max_length=100, null=True, blank=True, )

  def __str__(self):
    return self.course

        
    


class Application(models.Model):
  first_name = models.CharField(null=True, max_length=40)
  other_names = models.CharField(null=True, max_length=50)
  campus = models.CharField(max_length=30, blank=True, null=True, choices=CAMPUS_CHOICES)
  study = models.CharField(max_length=20, choices=STUDYTIME_CHOICES, blank=True, null=True,)
  level = models.CharField(max_length=20, choices=LEVEL_CHOICES, blank=True, null=True,)
  course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)
  gender = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=True, null=True,)
  courses = models.BooleanField(blank=True, null=True,)
  Date_of_birth = models.CharField(null=True, max_length=15)
  email = models.EmailField(null=True)
  phone = models.CharField(null=True, max_length=20)
  residence = models.TextField(null=True)
  nationality = models.TextField(null=True)
  where = models.TextField(null=True)
  file1 = models.FileField(null=True, blank=True)
  file2 = models.FileField(null=True, blank=True)
  file3 = models.FileField(null=True, blank=True)
  other_contact = models.TextField(null=True)
    
  class Meta:
    verbose_name = "Applications"
    verbose_name_plural = "Applications"
