from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
import random

from customer.models import Status
from . import models
from . import forms

# Create your views here.

def randomNum():
    return int(random.uniform(1000000000, 9999999999))

def index(request):
    try:
        acttive_user = Status.objects.get(user_name = request.user)
    except:
        acttive_user = Status()
        acttive_user.account_number = randomNum()
        acttive_user.balance = 0
        acttive_user.user_name = request.user
        acttive_user.save()
    return render(request, 'customer/home.html', {"active_user": acttive_user})

def money_transfer(request):
    if request.method == "POST":
        form = forms.TransferForm(request.POST)
        if form.is_valid():
            form.save()

            active_user = models.Transfer.objects.get(enter_username = request.user)
            receiver_acc_num = active_user.enter_username
            temp = active_user

            receiver_details = models.Status.objects.get(account_number = receiver_acc_num)
            transfer_amount = active_user.amount
            active_user = models.Status.objects.get(user_name = request.user)

            active_user.balance = active_user.balance - transfer_amount
            receiver_details.balance = receiver_details.balance + transfer_amount

            active_user.save()
            receiver_details.save()

            temp.delete()

        return redirect("customer/home.html")
    else:
        form = forms.TransferForm()
    return render(request, "customer/transfer.html", {"form": form})