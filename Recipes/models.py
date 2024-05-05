from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    time_to_cook = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    recepie_image = models.ImageField(upload_to="recepie")

    def __str__(self):
        return self.title
