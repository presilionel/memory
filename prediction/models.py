from django.utils import timezone
from django.db import models


# Create your models here.
class DataCEM(models.Model):
    dcem_id : models.AutoField(primary_key=True)
    dcem_path: models.FileField(upload_to='File/DATACEM')
    dqoe_path: models.FileField(upload_to='File/DATAQOE')
    predicted_path: models.FileField(upload_to='File/DATAMOS')
    prevision_path: models.FileField(upload_to='File/DATAMOS')
    dcem_upload_at: models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.dcem_id 
    
    def save(self):
        if not self.id:
            last_obj = DataCEM.objects.last()
            if last_obj:
                self.id = last_obj.id +1
            else:
                self.id = 1
        super(DataCEM, self).save()

    