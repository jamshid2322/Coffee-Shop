
from django.urls import path
from .views import home , coffee1 , about , blog , contact


urlpatterns = [
    path("", home, name='home'),
    path("coffee1/", coffee1, name='coffee1'),
    path("about/", about, name='about'),
    path("blog/", blog, name='blog'),
    path("contact/", contact, name='contact'),
]

