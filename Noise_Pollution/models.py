from django.db import models
# Create your models here.

class Sensore(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.BooleanField() # 0 digitale, 1 analogico
    location = models.CharField(max_length=50)


    def is_analogic(self):
        return self.type

class Dati(models.Model):
     sensore = models.ForeignKey(Sensore, on_delete=models.CASCADE)
     date = models.DateField(auto_now_add=True)
     time = models.TimeField(auto_now_add=True)
     analogic_value = models.IntegerField(default=-1)
     digital_value = models.BooleanField(null=True)







