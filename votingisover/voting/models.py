from django.db import models

# Create your models here.

class VotingInformation(models.Model):
    type = models.CharField(max_length=100)
    variantFirstCnt = models.IntegerField()
    variantSecondCnt = models.IntegerField()

class VotingDescription(models.Model):
    header = models.CharField(max_length=1024)
    variantFirstDescr = models.CharField(max_length=1000)
    variantSecondDescr = models.CharField(max_length=1000)
    info = models.ForeignKey(VotingInformation, on_delete = models.CASCADE)
