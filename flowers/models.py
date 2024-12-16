from django.db import models

class FlowerType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Flower(models.Model):
    type = models.ForeignKey(FlowerType, related_name="flowers", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
