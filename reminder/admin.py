from django.contrib import admin

# Register your models here.
from reminder.models import Author, Quotes

admin.site.register(Author)
admin.site.register(Quotes)