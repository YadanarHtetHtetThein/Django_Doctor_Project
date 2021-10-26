from django.db import models

class Doctor_Category(models.Model):
    icon = models.CharField(max_length=200)
    name_mm = models.CharField(max_length=255)
    name_eng = models.CharField(max_length=255)

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    qualifications = models.TextField()
    duty = models.TextField()
    category = models.IntegerField()

