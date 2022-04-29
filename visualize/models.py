from django.db import models
from django.contrib.auth.models import User as U

class Labeling(models.Model):
    user = models.ForeignKey(U, on_delete=models.DO_NOTHING, null=True)
    ground_Y = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

class Result(models.Model):
    predict_3class = models.TextField()
    confidence_3class = models.FloatField()
    predict_9class = models.TextField()
    confidence_9class = models.FloatField()

class Image(models.Model):
    filename = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    labeling = models.ForeignKey(Labeling, on_delete=models.DO_NOTHING, null=True)
    result = models.ForeignKey(Result, on_delete=models.DO_NOTHING, null=True)