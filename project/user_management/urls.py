"""
URL configuration for user_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


""" django.urls'den include() işlevini cagirarak users-app'in
uygulama urls modülünü(users/urls.py) ana projenin urls modülüne(user-mamagent/urls.py) dahil etmemiz gerekiyor. """
""" bu dosyanin amaci ana projenin urls.py dosyasina users-app'in urls.py dosyasini dahil etmektir. """

from django.contrib import admin
from django.urls import path, include                   # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("users.urls")),               # new
]