from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
from .models import Myself
# Create your views here.
def myself(request):
    myselfs = Myself.objects.all()
    return render(request, 'myself.html', {'myselfs': myselfs})

def index(request):
    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'Tanvir'
    # feature1.details = 'Tanvir Ahmed Software Engineer'
    # feature1.is_true = True

    # feature2 = Feature()
    # feature2.id = 1
    # feature2.name = 'Zahid'
    # feature2.details = 'Zahid Ahmed Software Engineer'
    # feature2.is_true = False

    
    features = Feature.objects.all()
    #to make dynamic, pass the data
    #name = 'Tanvir'
    # context = {
    #     'name': 'Tanvir',
    #     'age': 26,
    #     'nationality': 'Bangladeshi',
    # }
    return render(request, 'index.html', {'features': features})#, context)

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password is not same')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'credentials invalid')
            return redirect ('login')
        
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')