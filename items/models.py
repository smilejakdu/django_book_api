from django.db import models

# Create your models here.

class Kyobo(models.Model):
    image  = models.CharField(max_length=500 , null=True)
    title  = models.CharField(max_length=250)
    price  = models.CharField(max_length=200)
    review = models.CharField(max_length=500 , null=True)

    class Meta:
        db_table='kyobos'
