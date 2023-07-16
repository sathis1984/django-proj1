from django.contrib import admin
from crudapp.models import Books

# Register your models here.
class BooksAdmin(admin.ModelAdmin):
    list_display=['title','auth_name','pages','price']
admin.site.register(Books,BooksAdmin)