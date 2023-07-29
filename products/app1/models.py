from django.db import models

# Create your models here.


class product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=20,decimal_places=2)
    description = models.TextField()
    stars = models.IntegerField()


    def __str__(self):
        return self.name



