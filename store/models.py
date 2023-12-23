from django.db import models



# Create your models here.


class About(models.Model):
    image = models.ImageField(upload_to='about_media/')
    name =  models.CharField(max_length=100)
    profile = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    address = models.TextField(max_length=200)
    # description = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

    def __str__(self):
             return self.name
        

class Service(models.Model):
    image = models.ImageField(upload_to='service_media/')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, default= None)
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length= 250)
    lon_discription = models.CharField(max_length=500, default= 0)
    ordering = models.IntegerField(blank=True, null= True)

    def __str__(self):
            return self.title
        

class Category(models.Model):
    name =  models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_media/', blank=True, null= True)
   

    class Meta:
        
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name

        
class Blog(models.Model):
    image = models.ImageField(upload_to='blog_media/')
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length= 250)
    ordering = models.IntegerField(blank=True, null= True)

    def __str__(self):
            return self.title
    
        


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.EmailField()
    message = models.CharField(max_length=250)

    def __str__(self):
            return self.first_name
