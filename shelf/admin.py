from django.contrib import admin

from .models import Author, Publisher, Book, BookCategory, BookEdition,BookItem


class AuthorAdmin(admin.ModelAdmin):

    search_fields = ['first_name', 'last_name']
    ordering = ['last_name']


class BookAdmin(admin.ModelAdmin):

    search_fields = ['title']
    fields = ['title', 'authors', 'categories']
    list_display = ['title']

class BookCategoryAdmin(admin.ModelAdmin):

    search_fields = ['name']
    fields = ['name']

class BookEditionAdmin(admin.ModelAdmin):

    search_fields = ['book', 'isbn']
    fields = ['book', 'isbn', 'date', 'publisher']

class BookItemAdmin(admin.ModelAdmin):

    search_fields = ['catalogue_number']
    fields = ['catalogue_number', 'cover_type']

# Register your models here.

admin.site.register(BookItem, BookItemAdmin)
admin.site.register(BookEdition, BookEditionAdmin)
admin.site.register(BookCategory,BookCategoryAdmin)
admin.site.register(Book, BookAdmin)

admin.site.register(Author, AuthorAdmin)

admin.site.register([Publisher])