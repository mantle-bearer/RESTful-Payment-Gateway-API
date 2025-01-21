from django.db import models

# Create your models here.

#Payment model with customer name, email, amount, status and reference
class Payment(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='pending')
    reference = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.customer_name} - {self.amount}"
