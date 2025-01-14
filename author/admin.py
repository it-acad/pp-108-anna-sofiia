from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic')  # Поля для відображення у списку
    list_filter = ('surname', 'name')  # Фільтри
    search_fields = ('name', 'surname', 'patronymic')  # Поля для пошуку
    fieldsets = (
        ('Основна інформація', {
            'fields': ('name', 'surname', 'patronymic')
        }),
        ('Додаткові дані', {
            'fields': ('books',),
        }),
    )
    filter_horizontal = ('books',)  # Зручний вибір для ManyToMany полів
