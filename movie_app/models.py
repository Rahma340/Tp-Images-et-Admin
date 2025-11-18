from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.IntegerField()
    image = models.ImageField(upload_to='movies/', blank=True, null=True)
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return self.title
