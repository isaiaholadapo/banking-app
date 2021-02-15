from django import forms
from . import models

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