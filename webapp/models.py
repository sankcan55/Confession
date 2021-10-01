from django.db import models

# Create your models here.
class Feed(models.Model):
    name = models.CharField(max_length=500)
    title = models.CharField(max_length=7000)
    message = models.CharField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
