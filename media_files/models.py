from django.db import models

class MediaManager(models.Manager):
    def audio(self):
        return self.filter(type='Audio')

    def video(self):
        return self.filter(type='Video')

    def image(self):
        return self.filter(type='Image')

class Media(models.Model):
    MEDIA_TYPES = [
        ('Audio', 'Audio'),
        ('Video', 'Video'),
        ('Image', 'Image'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    format = models.CharField(max_length=10)
    size = models.DecimalField(max_digits=10, decimal_places=2)  # Size in MB
    duration_secs = models.IntegerField(default=0)  # Duration in seconds

    objects = MediaManager()

    def __str__(self):
        return self.name
