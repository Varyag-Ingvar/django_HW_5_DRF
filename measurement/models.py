from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Sensor')
    description = models.CharField(max_length=80, verbose_name='Description')

    class Meta:
        ordering = ['-id']


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Temperature')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Date')

    class Meta:
        ordering = ['-created_at']




