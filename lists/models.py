from django.db import models

class List(models.Model):
    pass

    # this is to get rid of the pylint .objects warning
    objects = models.Manager()

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

    # this is to get rid of the pylint .objects warning
    objects = models.Manager()