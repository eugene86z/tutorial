from django.db import models


class propertyInfo(models.Model):
    address1 = models.CharField(max_length=150)
    City =  models.CharField(max_length=40)
    State = models.CharField(max_length=2)
    Zip =  models.CharField(max_length=10)
    status = models.CharField(max_length=20, default='Not Active')


    def __str__(self):  #string representation
        return self.address1


