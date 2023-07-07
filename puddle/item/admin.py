from django.contrib import admin

# Register your models here.

from .models import Category, Item

admin.site.register(Category)
admin.site.register(Item)
# This code imports the admin module and the Category model from the item application.
# The last line registers the Category model with the admin site.



