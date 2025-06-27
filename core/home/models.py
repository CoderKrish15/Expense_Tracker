from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Use CASCADE for tighter data control
    salary = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)  # Optional: for tracking

    def __str__(self):
        return f"{self.name} - ₹{self.price} by {self.user.username}"
