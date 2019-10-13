from django.db import models
from datetime import datetime
from  django.contrib.auth.models import User

# Create your models here.
class Feeds(models.Model):
    UserID = models.ForeignKey(User,on_delete=models.CASCADE)
    PostTitle= models.CharField(max_length=200)
    PostMessage=models.TextField(blank=True)
    Image = models.ImageField(upload_to='photos', blank=False)
    Catagory=models.CharField(max_length=200)
    DateTime=models.DateTimeField(default=datetime.now,blank =False)

    def __str__(self):
        return self.PostTitle