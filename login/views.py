from django.shortcuts import redirect, render
from .models import info

# Create your views here.
def home(request):
    all_data = info.objects.all
    return render(request, 'home.html',{"all":all_data})

def login(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        email = request.POST.get('Email')
        password = request.POST.get('password')
            
        A = info(Name = Name, Email = email, password = password)
        A.save()

        all_data = info.objects.all
        print(all_data)
    return render(request, 'home.html',{"all":all_data})

def delete_event(request,pk):
    event = info.objects.get(pk=pk)
    event.delete()
    return redirect('home')

