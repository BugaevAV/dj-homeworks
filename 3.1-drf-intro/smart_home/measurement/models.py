from django.db import models



class Sensor(models.Model):

    name = models.CharField(max_length=10)
    description = models.CharField(max_length=50)


class Measurement(models.Model):
    
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(max_length=4)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', null=True)
    