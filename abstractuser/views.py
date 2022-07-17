from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login as authlogin

# Create your views here.
def login(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'),
                                         password=request.POST.get('password'))
        if user != None:
            authlogin(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect(reverse('staff'))
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse("staffq"))
            else:
                return HttpResponseRedirect(reverse("hacking"))
        else:
            a = messages.error(request, "Foydalanuvchi nomi yoki Parol xato")
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')