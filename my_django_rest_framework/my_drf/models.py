from django.db import models


class Cucumber(models.Model):
    title = models.CharField(max_length=150)
