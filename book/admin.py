from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Поля, які будуть відображатися у списку
    list_display = ('id', 'name', 'description', 'count')
    # Поля для фільтрування
    list_filter = ('count',)
    # Поля для пошуку
    search_fields = ('name', 'description')
    # Групування полів у деталізованому поданні
    fieldsets = (
        ('Основна інформація', {
            'fields': ('name', 'description', 'count'),
        }),
    )
