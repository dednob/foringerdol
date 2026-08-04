import uuid
from django.db import models
from events.models import Event


def generate_filename(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = "foringPackage_%s.%s" % (uuid.uuid4(), extension)
    return new_filename


# Create your models here.
class Package(models.Model):
    package_name = models.CharField(max_length=200)
    package_image = models.ImageField(upload_to=generate_filename, null=True)
    banner_image = models.ImageField(upload_to=generate_filename, null=True)
    price = models.FloatField()
    details = models.TextField(null=True)
    slug = models.SlugField(max_length=255, null=True, unique=True)
    event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE, related_name='packages')

    def __str__(self):
        return self.package_name
