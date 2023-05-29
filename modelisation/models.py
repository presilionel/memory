from django.db import models

# Create your models here.

class modelClass(models.Model):
    model_id: models.IntegerField()
    model_file: models.CharField(max_length=250)
    model_score: models.FloatField()
    def __str__(self):
        return self.model_id