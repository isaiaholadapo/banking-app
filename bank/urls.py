"""bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from account.views import (
    home_screen_view,
    login_view,
    logout_view,
    register_view,
    about_view,
    service_view,
    contact_view,
    
)
from customer.views import (
    money_transfer,
    index,
    deposit_view,
    withdraw_view,
    
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', home_screen_view, name = 'home'),
    path('about/', about_view, name = 'about'),
    path('service/', service_view, name = 'service'),
    path('contact/', contact_view, name = 'contact'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('register/', register_view, name = 'register'),
    path('transfer/', money_transfer, name = 'transfer'),
    path('u-account/', index, name = 'user_account'),
    path('deposit/', deposit_view, name = 'deposit'),
    path('withdraw/', withdraw_view, name = 'withdraw'),

]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
