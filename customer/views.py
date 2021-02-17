from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, authenticate
import random

from customer.models import Status
from . import models
from customer import forms

# Create your views here.

def randomNum():
    return int(random.uniform(1000000000, 9999999999))

def index(request):
    user = request.user
    if user.is_authenticated:
        try:
            acttive_user = Status.objects.get(user_name = request.user)
        except:
            acttive_user = Status()
            acttive_user.account_number = randomNum()
            acttive_user.balance = 0
            acttive_user.user_name = request.user
            acttive_user.save()
    else:
        return redirect('login')
    return render(request, 'customer/home.html', {"active_user": acttive_user})

def deposit_view(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            form = forms.DepositForm(request.POST)
            if form.is_valid():
                form.save()

                acti_user = models.Deposit.objects.get(dep_user_name = request.user)
                depositor_account_number = acti_user.dep_account
                temp = acti_user
                
                act_user = models.Status.objects.get(account_number = depositor_account_number)
                act_user_amout = acti_user.amount
                acti_user = models.Status.objects.get(user_name = request.user)
                

                acti_user.balance = acti_user.balance + act_user_amout

                acti_user.save()
                temp.delete()
               
                return redirect('user_account')
        else:
            form = forms.DepositForm()
    else:
        return redirect('login')
    return render(request, 'customer/deposit.html', {"form": form})

def withdraw_view(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            form = forms.WithdrawForm(request.POST)
            if form.is_valid():
                form.save()
                acti_user = models.Withdraw.objects.get(with_username = request.user)
                depositor_account_number = acti_user.with_account
                temp = acti_user
                
                act_user = models.Status.objects.get(account_number = depositor_account_number)
                act_user_amout = acti_user.amount
                acti_user = models.Status.objects.get(user_name = request.user)
                

                acti_user.balance =  acti_user.balance - act_user_amout

                acti_user.save()
                temp.delete()
               
                return redirect('user_account')

        else:
            form = forms.WithdrawForm()
    else:
        return redirect('login')
    return render(request, 'customer/withdraw.html', {"form": form})

def money_transfer(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            form = forms.TransferForm(request.POST)
            if form.is_valid():
                form.save()

                active_user = models.Transfer.objects.get(enter_username = request.user)
                receiver_acc_num = active_user.receiver_account_number
                temp = active_user

                receiver_details = models.Status.objects.get(account_number = receiver_acc_num)
                transfer_amount = active_user.amount
                active_user = models.Status.objects.get(user_name = request.user)

                if transfer_amount > active_user.balance:
                    raise ValueError("Your account balance is too low")
                else:
                    active_user.balance = active_user.balance - transfer_amount
                    receiver_details.balance = receiver_details.balance + transfer_amount

                active_user.save()
                receiver_details.save()

                temp.delete()

            return redirect("home")
        else:
            form = forms.TransferForm()
    else:
        return redirect('login')
    return render(request, "customer/transfer.html", {"form": form})