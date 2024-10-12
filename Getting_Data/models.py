from django.db import models


class Data_Getting(models.Model):
    Name=models.CharField(max_length=34)
    Father_Name=models.CharField(max_length=34)
    Mother_Name=models.CharField(max_length=43)
    
