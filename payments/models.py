from django.db import models
from django.core.exceptions import ValidationError
from rooms.models import Room


class Payment(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ('Mobile Money', 'Mobile Money'),
        ('Cash', 'Cash'),
    ]

    room = models.ForeignKey(Room, on_delete=models.PROTECT, related_name='payments')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES)
    payment_date = models.DateField()

    def clean(self):
        if self.amount is not None and self.amount <= 0:
            raise ValidationError({'amount': 'Amount must be greater than zero.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Payment of UGX {self.amount:,.0f} for Room {self.room.room_number} on {self.payment_date}"
