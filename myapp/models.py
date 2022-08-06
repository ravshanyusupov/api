from django.db import models


class Api(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=255)
    is_alive = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ' ' + self.last_name
