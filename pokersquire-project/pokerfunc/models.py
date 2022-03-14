from django.db import models


class Stats(models.Model):
    summary = models.CharField(max_length=200)
