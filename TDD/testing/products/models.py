from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()
    pub_date = models.DateField()

    @property
    def is_in_stock(self):
        return self.quantity > 0
