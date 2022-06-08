from .models import Product

# IMPLEMENTING DJANGO ORM

# Start by running the interactive Shell: 
# python manage.py shell

# 1---Inserting new record-----
s = Product(id="001",name="Strawberry", category="Fruits")
s.save()
# 2--------Retrieving all record-------------------
Product.objects.all()
# 3--------Filter Product record by their name--------
Product.objects.filter(name="Strawberry")
# 4--------Retrieving a single record--------
# with fieldname
single= Product.objects.get(id="001") 
# or with primary key
single= Product.objects.get(pk=001) 
# 5--------Changing a Product Price--------
single.price = 1000
single.save()