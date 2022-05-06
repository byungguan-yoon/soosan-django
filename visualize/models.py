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

class Data(models.Model):
    user = models.ForeignKey(U, on_delete=models.DO_NOTHING, null=True)
    dataset_start = models.DateTimeField()
    dataset_end = models.DateTimeField()

class AI_Model(models.Model):
    status = models.TextField()
    user = models.ForeignKey(U, on_delete=models.DO_NOTHING, null=True)
    dataset = models.ForeignKey(Data, on_delete=models.DO_NOTHING, null=True)
    train_start = models.DateTimeField(null=True)
    train_end = models.DateTimeField(null=True)
    score = models.FloatField(null=True)
    path = models.TextField(null=True)

class Deploy(models.Model):
    status = models.TextField()
    user = models.ForeignKey(U, on_delete=models.DO_NOTHING, null=True)
    ai_model = models.ForeignKey(AI_Model, on_delete=models.DO_NOTHING, null=True)
    deploy_start = models.DateTimeField(null=True)
    deploy_end = models.DateTimeField(null=True)
