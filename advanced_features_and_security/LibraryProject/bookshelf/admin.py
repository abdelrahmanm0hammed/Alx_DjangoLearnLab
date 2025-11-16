from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book , CustomUser
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

class CustomUserAdmin(UserAdmin):
    list_display = ('username','email')
    
admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)

