from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserDetails
from seller.models import Seller
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    return render(request, 'authentication/register.html')

def registerSave(request):

    if request.method == 'POST':
        
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        conf_password = request.POST.get('conf_password')
        is_seller = request.POST.get('seller_status')

        if password == conf_password:
            
            user = User()
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.set_password(conf_password)
            user.save()

            userDetails = UserDetails()
            userDetails.user = user
            userDetails.phone = phone
            if is_seller == "True":
                userDetails.is_seller = True
                seller = Seller()
                seller.user = user
                seller.save()

            userDetails.save()

        else:
            return HttpResponse("Wrong Password!")
    
    return redirect('login')

def loginn(request):
    return render(request, 'authentication/login.html')

def postLogin(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse("User not found")

        userLogin = authenticate(username = username, password = password)

        if userLogin is not None:
            login(request, userLogin)

            userDetails = UserDetails.objects.get(user = user)
            is_seller = userDetails.is_seller
            is_admin = userDetails.is_admin

            if is_seller:
                return render(request, 'seller/dashboard.html')

            return redirect('home')

        else:
            return HttpResponse("Check the details properly")

def logoutt(request):
    request.session.flush()
    logout(request)

    return redirect('home')