from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("blog", views.blog, name="blog"),
    path("cart", views.cart, name="cart"),
    path("checkout", views.checkout, name="checkout"),
    path("contact", views.contact, name="contact"),
    path("service", views.service, name="service"),
    path("shop", views.shop, name="shop"),
    path("thankyou", views.thankyou, name="thankyou"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)