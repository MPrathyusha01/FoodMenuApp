from django.db import models

# Create your models here.

class Item(models.Model):
    def __str__(self):
        return self.item_name
    
    item_name = models.CharField(max_length=200, default="Dummy")
    item_desc = models.CharField(max_length=200, default="No description")
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=200, default = "https://orders.goodthymes.ca/assets/img/goodthymes/default-menu-image-placeholder.png")
    