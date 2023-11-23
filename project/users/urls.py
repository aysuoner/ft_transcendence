from django.urls import path
from . import views # bu dizi içindeki views.py dosyasını kullan demektir.
from django.urls import path
# from . import views demek: bu dizindeki views.py dosyasını kullan demektir.

#urls.py içinde tanımlanan pathler ile views.py içinde tanımlanan fonksiyonlar eşleşir.
#urls.py bir nevi views.py'nin yönlendiricisidir.
#urlpattern içindeki parametlerin anlamları:
#1. parametre: url adresi
#2. parametre: views.py içinde tanımlanan fonksiyon
#3. parametre: path'e verilen isim. amacı: views.py içindeki fonksiyonu çağırırken kullanmak.

urlpatterns = [
    path('', views.home, name='users-home'),
	path('register/', views.RegisterView.as_view(), name='users-register'),
]
