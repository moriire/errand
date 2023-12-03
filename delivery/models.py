from django.db import models
class Items(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self) -> str:
        return self.name
    

class CartItems(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    unit = models.IntegerField(default=1)
    
    def __str__(self) -> str:
        return self.name