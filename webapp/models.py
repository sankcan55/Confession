from django.db import models

# Create your models here.
class Feed(models.Model):
    name = models.CharField(max_length=500)
    content = models.CharField(max_length=10000)
    def __str__(self):
        return self.name
