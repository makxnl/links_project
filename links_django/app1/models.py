from django.db import models

class Links(models.Model):
    link = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f'{self.description} {self.link}'

# class Users(models.Model):
#     username