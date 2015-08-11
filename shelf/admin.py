from django.contrib import admin

from .models import Author, Publisher, Book


class AuthorAdmin(admin.ModelAdmin):

    search_fields = ['first_name', 'last_name']
    ordering = ['last_name']


class BookAdmin(admin.ModelAdmin):

    search_fields = ['title']
    fields = ['title', 'authors']
    list_display = ['title']


# Register your models here.

admin.site.register(Book, BookAdmin)

admin.site.register(Author, AuthorAdmin)

admin.site.register([Publisher])