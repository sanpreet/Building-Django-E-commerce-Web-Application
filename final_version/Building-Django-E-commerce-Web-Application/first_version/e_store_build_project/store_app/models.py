from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=500)
    price = models.FloatField() 
    description = models.TextField()
    imagelink = models.CharField(max_length=800)

class order_details(models.Model):
    first_name= models.CharField(max_length=600)
    last_name = models.CharField(max_length=600)
    address = models.CharField(max_length=700)
    city = models.CharField(max_length=600)
    payment_method = models.CharField(max_length=600)
    payment_data = models.CharField(max_length=600)
    items = models.TextField()





