import uuid
from django.db import models


# Create your models here.
def generate_filename(instance, filename):
   extension = filename.split('.')[-1]
   new_filename = "foringPictures_%s.%s" % (uuid.uuid4(), extension)
   return new_filename


class Pictures(models.Model):
    
    header = models.ImageField(upload_to=generate_filename, null=True)
    promotionOne = models.ImageField(upload_to=generate_filename, null=True)
    promotionTwo = models.ImageField(upload_to=generate_filename, null=True)
    footer = models.ImageField(upload_to=generate_filename, null=True)

# Create your models here.
