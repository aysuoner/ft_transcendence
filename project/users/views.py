from django.shortcuts import render, redirect 
from django.contrib import messages
from django.views import View 
#from django.views import View demek: django.views içindeki View class'ını kullan demektir. view class get ve post methodlarını kullanmamızı sağlar.

from .forms import RegisterForm #users klasorundaki forms.py dosyaını buluyor ve içindeki RegisterForm class'ını kullanıyor.
 
from django.http import HttpResponse, Http404 #SPA


#views.py dosyasında requestlere response donduren fonksiyonlar bulunur.
# Create your views here.
#views.py içinde tanımlanan fonksiyonlar urls.py içinde tanımlanan pathler ile eşleşir.
#pathler ile eşleşen fonksiyonlar çalıştırılır.
#bu fonksiyonlar render ile bahsi gecen html sayfalarını çağırır.
#yani view.py'nin amaci html sayfalarini çağırmak ve bu sayfalari kullaniciya göstermektir.
#home(request) demek home.html sayfasini çağır demektir.

def home(request):
    return render(request, 'users/home.html')

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html' #burada Django içindeki forms classını override ederek kendi form classımızı oluşturduk.

    def get(self, request, *args, **kwargs): #İstek get ise, boş bir formun yeni bir örneğini oluşturur.
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

#İstek gönderiliyorsa, -- Gönderi verileriyle formun yeni bir örneğini oluşturur.
#Ardından form.is_valid() yöntemini çağırarak formun geçerli olup olmadığını kontrol eder. 
#Daha sonra form geçerliyse, temizlenen form verilerini işleyin ve kullanıcıyı veritabanımıza kaydedin.
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}') #home sayfasında kullanıcının giriş yaptığı username'i gösterilir. başarılı bir giriş olduğu için

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})
