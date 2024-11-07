from django.db import models

class temperature_db(models.Model):
    id = models.AutoField(primary_key=True)
    sensor_id = models.IntegerField(null=False)
    temperature = models.FloatField(null=False)
    humidity = models.FloatField(null=False)
    datetime = models.DateTimeField(null=False)
    



