from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from letters.models import Letter


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article',null=True)
    letter = models.ForeignKey(Letter,on_delete=models.SET_NULL,
                               related_name='letter',null=True,blank=True)
    title = models.CharField(max_length=100,null=False)
    image = models.ImageField(upload_to='article',null=True)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True,null=True)

    like = models.IntegerField(default=0)