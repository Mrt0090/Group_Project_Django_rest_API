from django.db import models
from django.core.validators import RegexValidator


class Mobiles(models.Model):
    ean = models.CharField( # primary key of 13 digits from barcode
        max_length=13,
        primary_key=True,
        validators=[
            RegexValidator(regex=r"^\d{13}$", message="EAN must be exactly 13 digits.")
        ],
        help_text="Enter a 13-digit EAN (only numbers).",
    )
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    
    def __str__(self):
        return f"{self.brand} {self.model}"
