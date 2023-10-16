from django.shortcuts import render,redirect
from .models import Band
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, 'myBand/home.html')

def about(request):
    return render(request, 'myBand/about.html')

def album_list(request):
    albums = Band.objects.all()
    return render(request, 'myBand/album_list.html', {'albums': albums})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'myBand/login.html')

def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'myBand/registration.html', {'form': form})