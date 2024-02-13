from django.db import models

class Inbound(models.Model):
    id= models.IntegerField(primary_key=True)
    reference = models.CharField(max_length=255, unique=True)
    date_received = models.IntegerField()
    product_sku = models.CharField(max_length=100)
    quantity = models.IntegerField()
    location = models.CharField(max_length=100)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.reference
