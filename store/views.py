from django.shortcuts import render, redirect, get_object_or_404
from store.models import About
from store.models import Service
from store.models import Blog
from store.forms import Contactform


# Create your views here.

def index(request):
    
    return render(request,'index.html')


# def service(request):
    
#     service = Service.objects.all().order_by('-id')

#     context = {
#         'service': service
#     }

#     return render(request, 'service.html',context)

def about(request):
   
    about = About.objects.first()
    # about = About.objects.get()

    context = {

            'about': about
        }

    return render(request, 'about.html', context)


def service(request):
    
    service = Service.objects.all().order_by('-id')

    context = {
        'service': service
    }

    return render(request, 'service.html',context)


def details_page(request, pk):
    obj = get_object_or_404(Service, pk = pk)
    
    context={
    
       'obj' : obj
    
    }
    
    return render(request, 'details.html', context)


def blog(request):
    
    blog = Blog.objects.all().order_by('ordering')

    context = {
        'blog': blog
    }

    return render(request, 'blog.html',context)










def contact(request):
    form = Contactform(request.POST)

    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('/')
        
    return render(request, 'contact.html', { 'form' : form})
