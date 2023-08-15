from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    discriptions = models.TextField()

    def __str__(self):
        return self.title