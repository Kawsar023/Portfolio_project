from django.urls import path
from .views import index, about, service, blog, contact, details_page

urlpatterns = [
    
    path('', index, name = 'index'),
    path('about', about, name= 'about-us'),
    path('service', service, name= 'service'),
    path('blog', blog, name= 'blog'),
    path('contact', contact, name='contact-us'),
    path('<int:pk>', details_page, name= 'details_page')
    
]
