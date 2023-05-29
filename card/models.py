from django.db import models

# Create your models here.
class SatisfactionPredicted(models.Model):
    satisfaction_id: models.IntegerField()
    predicted_file: models.CharField(max_length=250)
    model_id: models.CharField(max_length=250)

    def __str__(self):
        return self.satisfaction_id


