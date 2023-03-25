from django.db import models

class StudInfo(models.Model):
    uid = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    lattempt =models.IntegerField(default=0)
    accno = models.CharField(max_length=255)
    acc_balance = models.IntegerField()
    statement = models.FileField(upload_to="uploads")
