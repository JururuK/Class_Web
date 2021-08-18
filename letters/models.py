from django.db import models

# Create your models here.

class Letter(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='letter/',null=False)

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'