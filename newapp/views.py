from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import * # Create your views here.

def index(request):
    return render(request, "app/index.html")

def blog(request):
    return render(request, "app/blog.html")

def cart(request):
    context = {}
    return render(request, "app/cart.html", context)

def checkout(request):
    context = {}
    return render(request, "app/checkout.html", context)

def contact(request):
    return render(request, "app/contact.html")

def about(request):
    return render(request, "app/about.html")

def service(request):
    return render(request, "app/service.html")

def shop(request):
    products = Product.objects.all()
    context = {'products': products}
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        
        myuser = newsletter.objects.create(username=username, email=email)
        myuser.save()
    
    return render(request, "app/shop.html", context)

def thankyou(request):
    return render(request, "app/thankyou.html")
