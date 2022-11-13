from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    contact=models.CharField(max_length=20)
    description=models.TextField(max_length=30)

    def __str__(self):
        return self.name
