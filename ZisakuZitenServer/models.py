from django.db import models

# Create your models here.

class Group(models.Model):
    title = models.CharField(max_length=64)
    updateTime = models.CharField(max_length=32)
    # ziten_updT_List = model




class Ziten(models.Model):
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=128)
    updateTime = models.CharField(max_length=32)
    group = models.ForeignKey(Group,related_name="ziten_updT_List",on_delete=models.CASCADE)



