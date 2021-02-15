from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CustomerDetails)
admin.site.register(Status)
admin.site.register(Transfer)
admin.site.register(Deposit)