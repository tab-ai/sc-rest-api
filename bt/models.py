from django.db import models

class Band(models.Model):
    dev_id = models.IntegerField(null=True)
    temp = models.FloatField(null=True)
    ber = models.FloatField(null=True)
    created = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.dev_id

