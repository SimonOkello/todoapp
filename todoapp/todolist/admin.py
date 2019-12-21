from django.contrib import admin
from todolist.models import Category, Todolist

# Register your models here.
admin.site.register(Category)
admin.site.register(Todolist)
