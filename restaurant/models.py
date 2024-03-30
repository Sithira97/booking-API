from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    guest_number = models.SmallIntegerField()
    date_of_reservation = models.DateField()
    comment = models. TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}  - {self.date_of_reservation}"


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

    def __str__(self):
        return f"{self.title}  - {self.inventory}"