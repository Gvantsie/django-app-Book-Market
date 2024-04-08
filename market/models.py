from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    best_seller = models.BooleanField(default=False)
    age_group = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)

    def __str__(self):
        return self.title
