from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from letters.models import Letter


class Subscription(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,
                             related_name='subscription',null=False)
    letter = models.ForeignKey(Letter,on_delete=models.CASCADE,
                                related_name='subscription',null=False)

    class Meta:
        unique_together=['user','letter']