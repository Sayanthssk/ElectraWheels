from django.db import models

# Create your models here.

class Feedback_model(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    feedback = models.CharField(max_length=100, null=True, blank=True)
    reply = models.CharField(max_length=100, null=True, blank=True)

class Complaint_model(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    complaint = models.CharField(max_length=100, null=True, blank=True)