from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=10)
    buy_rate = models.DecimalField(max_digits=10, decimal_places=2)
    sell_rate = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.date})"
