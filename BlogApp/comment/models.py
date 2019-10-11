from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Comments(models.Model):
    UserID = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    PostID=models.IntegerField(blank=False)
    Comment= models.TextField(blank=False)
    DateTime=models.DateTimeField(default=datetime.now,blank =False)
    
    def __str__(self):
        return self.Comment