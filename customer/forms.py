from django import forms
from . import models
from django.contrib.auth import authenticate

class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = models.CustomerDetails
        fields = ['fullname', 'sex', 'email', 'phone_number', 'user_name']

class TransferForm(forms.ModelForm):
    class Meta:
        model = models.Transfer
        fields = ['enter_username', 'receiver_account_number', 'amount']
    
        

class DepositForm(forms.ModelForm):
    class Meta:
        model = models.Deposit
        fields = ['amount', 'dep_user_name', 'dep_account']

class WithdrawForm(forms.ModelForm):
    class Meta:
        model = models.Withdraw
        fields = ['amount', 'with_account', 'with_username']