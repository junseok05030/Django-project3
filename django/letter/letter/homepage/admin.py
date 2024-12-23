from django.contrib import admin

# Register your models here.
from homepage.models import Author, Mail


admin.site.register(Author)
admin.site.register(Mail)
