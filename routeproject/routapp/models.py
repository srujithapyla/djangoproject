from django.db import models

# Create your models here.


class routemodel(models.Model):
    name=models.CharField(max_length=123)
    age=models.IntegerField()
    Gender=models.CharField(max_length=123)

    class Meta:
        db_table='route_table'