from django.db import models

class Item(models.Model):
    text = models.TextField(default='')

    # this is to get rid of the pylint .objects warning
    objects = models.Manager()