from django.db import models

class Team(models.Model):
    name            = models.CharField(max_length=50)
    designation     = models.CharField(max_length=50)
    description     = models.TextField()
    profile_image   = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name
