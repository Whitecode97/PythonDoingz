from django.contrib import admin
from .models import Addres, Bio, Doctor, People, Product
# Register your models here.

# admin.site.register(Post)
admin.site.register(People)
admin.site.register(Doctor)
admin.site.register(Addres)
admin.site.register(Bio)
admin.site.register(Product)