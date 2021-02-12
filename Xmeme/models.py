from django.db import models

# Create your models here.
class memes(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    captions = models.CharField(max_length=255)

    def __str__(self):
        return self.name
