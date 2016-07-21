from django.db import models


class investmentInfo(models.Model):
    propAddress = models.CharField(max_length=250)
    requested_funding =  models.CharField(max_length=20)
    credit = models.CharField(max_length=4)
    estimated_return =  models.CharField(max_length=10)
    status = models.CharField(max_length=20, default='Not Active')


    def __str__(self):  #string representation
        return self.propAddress
