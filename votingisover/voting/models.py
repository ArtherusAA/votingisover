from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Voting(models.Model):
    type = models.CharField(max_length=100)
    header = models.CharField(max_length=1024)

class Variant(models.Model):
    text = models.CharField(max_length=1024)
    voting_id =  models.ForeignKey(Voting, on_delete = models.CASCADE)

class Vote(models.Model):
    date = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    variant_id = models.ForeignKey(Variant, on_delete = models.CASCADE) #Вариант из формыыыы
