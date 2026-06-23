from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock_left=models.IntegerField(default=0)
    listed_time=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')

    image=models.ImageField(upload_to='products/',blank=True,null=True)

    def __str__(self):
        return self.name