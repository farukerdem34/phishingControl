from django.db import models

class Name(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    count = models.IntegerField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"