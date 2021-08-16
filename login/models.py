from django.db import models

# Create your models here.
class info(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=20)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.Name