from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(blank=True,null=True,upload_to='service')

    def __str__(self):
        return self.name
