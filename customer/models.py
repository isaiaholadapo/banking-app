from django.db import models
import datetime
# Create your models here.

class CustomerDetails(models.Model):
    fullname            = models.CharField(max_length = 50)
    sex                 = models.CharField(max_length = 1 )
    email               = models.EmailField(unique = True)
    phone_number        = models.IntegerField(default = 0)
    user_name           = models.CharField(max_length =  50)

class Status(models.Model):
    account_number      = models.IntegerField()
    balance             = models.IntegerField()
    user_name           = models.CharField(max_length =  50)

class Transfer(models.Model):
    enter_username              = models.CharField(max_length = 50)
    receiver_account_number     = models.IntegerField()
    amount                      = models.IntegerField()

class Deposit(models.Model):
    amount                  = models.IntegerField()
    dep_account             = models.IntegerField(default = 0)
    dep_user_name           = models.CharField(max_length =  50, default = None)
