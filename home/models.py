from django.db import models

# Create your models here.
# class Post (models.Model):
#     post_title = models.CharField(max_length=10000)
#     post_content = models.CharField(max_length=100000)
#     date_posted = models.DateTimeField(auto_now_add=True)
    
class People (models.Model):
    name = models.CharField(max_length=10000)
    username = models.CharField(max_length=10000)
    email = models.EmailField()
    medical_case = models.CharField(max_length=100000)
    date_joined = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey("Addres", on_delete= models.CASCADE)
    
    def __str__(self):
        return self.username
    
class Doctor (models.Model):
    name = models.CharField(max_length=10000)
    email = models.EmailField()
    specialty = models.CharField(max_length=10000)
    patients = models.ForeignKey("People", on_delete= models.CASCADE)
    date_joined= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.specialty

class Product(models.Model):
    id = models.CharField(max_length=10000, primary_key=True)
    name = models.CharField(max_length=10000)
    category = models.CharField(max_length=10000)
    price = models.CharField(max_length=10000)
    date_registered = models.DateTimeField(auto_now_add=True)
    
class Addres (models.Model):
    street = models.CharField(max_length=10000)
    city= models.CharField(max_length=10000)
    country = models.CharField(max_length=100000)
    def __str__(self):
            return self.city
    
class Bio(models.Model):
    usernames= models.OneToOneField(People, on_delete= models.CASCADE)
    content = models.CharField(max_length=100000)
    def __str__(self):
            return self.content