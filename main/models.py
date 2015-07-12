from django.db import models

# *****************************************************************************
# class: Buy
# *****************************************************************************


class Buy(models.Model):
    is_complete = models.BooleanField(default=False)
    date_create = models.DateField(auto_now_add=True)
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
