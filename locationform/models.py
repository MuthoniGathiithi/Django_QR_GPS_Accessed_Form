from django.db import models
class LocationRestrictedForm(models.Model):
    title =models.CharField(max_length=200)
    description = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    def __str__(self):
        return self.title
    
    class Meta:
        unique_together = ('form', 'email', 'submitted_at__date')
    
class AttendanceSubmission(models.Model):
    form=models.ForeignKey(LocationRestrictedForm, on_delete=models.CASCADE)  
    name= models.CharField(max_length=100)
    location_accuracy = models.FloatField(null=True, blank=True)
    email = models.EmailField()
    present=models.BooleanField(default=False)
    Submitted_at = models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        return f"{self.name} - {self.form.title}"