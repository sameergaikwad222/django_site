from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser, User
import django.contrib.auth.backends
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    print(request.user, " ", request.user.is_anonymous)
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, phone=phone, email=email,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been sent !')

    return render(request, 'contacts.html')


def logIn(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get(
            'uname'), password=request.POST.get('pass'))

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.success(request, 'Successfully Logged In !')
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            print("Not Able to authenticate")
            messages.warning(request, 'Invalid Login Credentials !')
            return render(request, 'login.html')

    return render(request, 'login.html')


def logoff(request):
    logout(request)
    messages.success(request, 'Visit Again')
    return render(request, 'logoff.html')
