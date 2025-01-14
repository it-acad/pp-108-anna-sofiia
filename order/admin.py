from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Поля, які будуть відображатися у списку
    list_display = ('id', 'book', 'user', 'created_at', 'plated_end_at', 'end_at')
    # Поля для фільтрування
    list_filter = ('created_at', 'end_at', 'plated_end_at')
    # Поля для пошуку
    search_fields = ('book__name', 'user__email')
    # Групування полів у деталізованому поданні
    fieldsets = (
        ('Основна інформація', {
            'fields': ('user', 'book', 'created_at'),
        }),
        ('Деталі замовлення', {
            'fields': ('plated_end_at', 'end_at'),
        }),
    )
    # Тільки для перегляду поля `created_at`, яке не можна змінити
    readonly_fields = ('created_at',)
