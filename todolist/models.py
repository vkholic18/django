from django.db import models

from django.contrib.auth.models import User


class Tasks(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    desc=models.CharField(max_length=300)
