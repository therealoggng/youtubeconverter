from django.db import models




class Converter(models.Model):
    link = models.URLField(blank=False)
    email = models.EmailField(max_length=255)

