from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('what_we/', what_we, name='what_we'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
]