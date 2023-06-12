from django.utils import timezone
from django.db import models

# Create your models here.

class modelClass(models.Model):
    model_id: models.IntegerField()
    model_file: models.CharField(max_length=250)
    model_score: models.FloatField()
    model_path: models.FileField()
    def __str__(self):
        return self.model_id

class DataCEM(models.Model):
    dcem_id : models.IntegerField()
    dcem_path: models.FileField(upload_to='File/DATACEM')
    dcem_upload_at: models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.dcem_id 


class Dataqoe(models.Model):
    dqoe_id : models.IntegerField()
    dqoe_path: models.FileField(upload_to='File/DATAQOE')
    dqoe_upload_at: models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.dqoe_id

class DataMOS(models.Model):
    dmos_id : models.IntegerField()
    dmos_path: models.FileField(upload_to='File/DATAMOS')
    dmos_upload_at: models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.dmos_id

class DataPredicted(models.Model):
    predicted_id : models.IntegerField()
    predicted_path: models.FileField(upload_to='File/DATAMOS')
    predicted_at: models.DateTimeField(default=timezone.now)
    predicted_on : models.FileField()
    def __str__(self):
        return self.predicted_id
    
class DataPrevision(models.Model):
    prevision_id : models.IntegerField()
    prevision_path: models.FileField(upload_to='File/DATAMOS')
    prevision_at: models.DateTimeField(default=timezone.now)
    prevision_on : models.FileField()
    def __str__(self):
        return self.prevision_id