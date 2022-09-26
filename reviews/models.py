from django.db import models

# Create your models here.

class Review(models.Model):
    # image =  models.CharField(max_length=100)
    reviewer_name = models.CharField(max_length=500, null=True)
    title = models.CharField(max_length=500)
    review = models.TextField(null=True)
# Create your models here.