from django.db import models
class LocationRestrictedForm(models.Model):
    title =models.CharField(max_length=200)
    description = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    def __str__(self):
        return self.title
    
    