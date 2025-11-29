from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    title = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=15)
    category = models.CharField(max_length=50)
    date = models.DateField()

    def _str_(self):
        return f"{self.title} - {self.user.username}"