from django.db import models
import datetime
# Create your models here.

class CustomerDetails(model.Models):
    fullname            = models.CharField(max_length = 50)
    sex                 = models.CharField(max_length = 1 )
    email               = models.EmailField(unique = True)
    phone_number        = models.IntegerField(default = 0)
    user_name           = models.CharField(max_length =  50)

class Status(model.Models):
    account_number      = model.IntegerField()
    balance             = models.IntegerField()
    user_name           = models.CharField(max_length =  50)

class Transfer(model.Models):
    enter_username              = model.CharField(max_length = 50)
    receiver_account_number     = models.IntegerField()
    amount                      = models.IntegerField()