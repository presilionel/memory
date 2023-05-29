from django.db import models

# Create your models here.

class predictionClass(models.Model):
    prediction_id: models.CharField(max_length=250)
    model_id: models.CharField(max_length=250)
    model_score: models.FloatField()
    data_file: models.CharField(max_length=250)
    predicted_file: models.CharField(max_length=250)

    def __str__(self):
        return self.prediction_id