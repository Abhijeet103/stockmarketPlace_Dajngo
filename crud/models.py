from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Stock(models.Model) :
    ticker = models.CharField(max_length=10 , primary_key=True)
    name  =  models.CharField(max_length=200)
    description  =  models.CharField(max_length=5000)
    curr_price  =   models.FloatField()

    def __str__(self):
        return  self.name


class UserStock(models.Model) :
    user =  models.ForeignKey(User ,  on_delete=models.CASCADE)
    stock  = models.ForeignKey(Stock ,  on_delete= models.CASCADE)
    buyPrice  =  models.FloatField()
    buyQuantity =  models.IntegerField()
    purchaseDate =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.stock.name + " " + str(self.buyPrice)
