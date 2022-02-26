from django.db import models 

# Create your models here.
class Post(models.Model):
    description = models.TextField(max_length=500)
    quanitity = models.IntegerField()
    
