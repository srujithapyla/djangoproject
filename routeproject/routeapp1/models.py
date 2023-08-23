from django.db import models

# Create your models here.
class routemodel1(models.Model):
    name1=models.CharField(max_length=123)
    age1=models.IntegerField()
    Gender1=models.CharField(max_length=123)

    class Meta:
        db_table='route_table1'