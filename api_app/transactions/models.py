from django.db import models

class Transaction(models.Model):
    reference   = models.IntegerField()
    timestamp   = models.DateTimeField()
    amount      = models.IntegerField()
    currency    = models.CharField(max_length=10)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.description