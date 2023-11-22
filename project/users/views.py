from django.shortcuts import render

# Create your views here.
#views.py içinde tanımlanan fonksiyonlar urls.py içinde tanımlanan pathler ile eşleşir.
#pathler ile eşleşen fonksiyonlar çalıştırılır.
#bu fonksiyonlar render ile bahsi gecen html sayfalarını çağırır.
#yani view.py'nin amaci html sayfalarini çağırmak ve bu sayfalari kullaniciya göstermektir.
#home(request) demek home.html sayfasini çağır demektir.
def home(request):
    return render(request, 'users/home.html')