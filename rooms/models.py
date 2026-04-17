from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Room(models.Model):
    CATEGORY_CHOICES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Suite', 'Suite'),
        ('Deluxe', 'Deluxe'),
    ]

    room_number = models.IntegerField(unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_occupied = models.BooleanField(default=False)

    def clean(self):
    # Check if room_number is not None before comparing
        if self.room_number is not None:
            if self.room_number <= 0:
                raise ValidationError({'room_number': "Room number must be positive."})
    
    # Check if price_per_night is not None before comparing
        if self.price_per_night is not None:
            if self.price_per_night <= 0:
                raise ValidationError({'price_per_night': "Price must be greater than zero."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Room {self.room_number}"
