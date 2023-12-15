
# Create your views here.
# sharon/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my homepage!")

def additional_page(request):
    return HttpResponse("This is my additional page.")

#14/12/2023
# Sharon/views.py
# Sharon/views.py
from django.shortcuts import render, redirect
from .forms import UserInformationForm
from .models import UserInformation  # Add this import statement

def home(request):
    if request.method == 'POST':
        form = UserInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('additional_page')
    else:
        form = UserInformationForm()

    return render(request, 'home.html', {'form': form})

def additional_page(request):
    user_info = UserInformation.objects.last()
    return render(request, 'additional_page.html', {'user_info': user_info})
