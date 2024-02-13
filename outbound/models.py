from django.db import models

class Outbound(models.Model):

    id= models.IntegerField(primary_key=True)
    reference = models.CharField(max_length=255, unique=True)
    date_shipped = models.IntegerField()
    product_sku = models.CharField(max_length=100)
    quantity = models.IntegerField()
    destination = models.CharField(max_length=255)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.reference} - {self.product_sku}"

