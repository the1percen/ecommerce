from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from .models import * # Create your views here.

def index(request):
    return render(request, "app/index.html")

def blog(request):
    return render(request, "app/blog.html")

from django.shortcuts import render
from .models import Order

def cart(request):
    if request.user.is_authenticated:  # Use request.user instead of request.User
        customer = request.user.customer  # Assuming a one-to-one relationship
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()  # Ensure this matches the related name
    else:
        items = []
    context = {'items': items, 'order': order}
    return render(request, "app/cart.html", context)


def checkout(request):
    context = {}
    return render(request, "app/checkout.html", context)

def contact(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        myuser = contactus.objects.create(firstname=firstname, lastname=lastname, email=email, message=message)
        myuser.save()
        
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
