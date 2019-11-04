from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()

    def __str__(self):
        return self.name
    

class Client(models.Model):
    name = models.CharField(max_length=50)    
    cpf = models.CharField(max_length=11)       

    def __str__(self):
        return self.name

class Cart(models.Model):
    dt_purchase = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE) 

    def __str__(self):
        return self.client

class Quantity(models.Model):
    quantity = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

  
    



