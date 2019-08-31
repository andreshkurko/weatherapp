from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30)

    def str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'
