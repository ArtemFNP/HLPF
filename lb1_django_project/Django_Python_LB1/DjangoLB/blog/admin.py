from django.contrib import admin
from .models import Category, Article, Comment # Переконайтеся, що всі три моделі імпортовані

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',) # Які поля показувати у списку категорій
    search_fields = ('name',) # За якими полями можна шукати

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publication_date', 'author', 'comment_count_display') # Поля у списку статей
    list_filter = ('publication_date', 'category', 'author') # Фільтри збоку
    search_fields = ('title', 'content') # Пошук
    date_hierarchy = 'publication_date' # Зручна навігація за датою

    def comment_count_display(self, obj):
        return obj.comment_count # Використовуємо property з моделі
    comment_count_display.short_description = 'К-сть коментарів' # Назва колонки

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'article', 'created_at', 'content_excerpt')
    list_filter = ('created_at', 'article')
    search_fields = ('author_name', 'content')

    def content_excerpt(self, obj, max_length=50):
        # Показуємо лише частину коментаря у списку
        if len(obj.content) > max_length:
            return obj.content[:max_length] + '...'
        return obj.content
    content_excerpt.short_description = 'Фрагмент коментаря'

# Або, якщо ви віддаєте перевагу старому стилю реєстрації (теж працює):
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Article, ArticleAdmin)
# admin.site.register(Comment, CommentAdmin)