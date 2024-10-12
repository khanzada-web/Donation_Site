from django.db import models


class Admin_panel(models.Model):
    Name=models.CharField(max_length=18)
    Reason=models.CharField(max_length=18)
    Descrption=models.TextField()
    img = models.ImageField(upload_to='img/', blank=True,null=True)
