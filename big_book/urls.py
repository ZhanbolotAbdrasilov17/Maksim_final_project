from django.conf.urls.static import static
from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('what_we/', what_we, name='what_we'),
    path('blog/', blog, name='blog'),
    path('mail/create/', MailCreateView.as_view(), name='mail_create'),
    path('contact/', contact, name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)