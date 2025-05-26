from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Category, Article, Comment # Переконайтеся, що всі три імпортовані

def category_list(request):
    categories_with_counts = Category.objects.annotate(num_articles=Count('articles')).order_by('name')
    print("----- CATEGORIES -----") # ДІАГНОСТИКА
    for cat in categories_with_counts: # ДІАГНОСТИКА
        print(f"Категорія: {cat.name}, Статей: {cat.num_articles}") # ДІАГНОСТИКА
    print("----------------------") # ДІАГНОСТИКА
    context = {
        'categories': categories_with_counts,
    }
    return render(request, 'blog/category_list.html', context)


def article_list_by_category(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    sort_by = request.GET.get('sort_by', 'date') # Отримуємо параметр сортування

    articles_in_category = Article.objects.filter(category=category) # Фільтруємо статті за категорією

    if sort_by == 'comments':
        articles = articles_in_category.annotate(
            num_comments_for_sorting=Count('comments')
        ).order_by('-num_comments_for_sorting', '-publication_date')
        current_sorting = 'Кількістю коментарів'
    else: # За замовчуванням або якщо sort_by == 'date'
        articles = articles_in_category.order_by('-publication_date')
        current_sorting = 'Датою публікації'
    
    print(f"----- ARTICLES IN CATEGORY '{category.name}' (sort_by: {sort_by}) -----") # ДІАГНОСТИКА
    for art in articles: # ДІАГНОСТИКА
        print(f"Стаття: {art.title}, Коментарів: {art.comment_count}") # ДІАГНОСТИКА
        if hasattr(art, 'num_comments_for_sorting'): # ДІАГНОСТИКА
             print(f"  Анотовано коментарів: {art.num_comments_for_sorting}") # ДІАГНОСТИКА
    print("-----------------------------") # ДІАГНОСТИКА

    context = {
        'articles': articles,
        'current_category': category, # Передаємо поточну категорію для відображення
        'current_sorting_param': sort_by,
        'current_sorting_text': current_sorting,
        'page_title': f"Статті в категорії: {category.name}" # Динамічний заголовок
    }
    # Ми можемо повторно використати шаблон article_list.html
    return render(request, 'blog/article_list.html', context)

def article_list(request): # <--- ОНОВЛЮЄМО ЦЮ ФУНКЦІЮ
    sort_by = request.GET.get('sort_by', 'date') # За замовчуванням сортуємо за датою
    print(f"----- ARTICLES (sort_by: {sort_by}) -----") # ДІАГНОСТИКА

    if sort_by == 'comments':
        # Анотуємо queryset кількістю коментарів для сортування
        # 'comments' - це related_name з ForeignKey в моделі Comment до Article
        articles_qs = Article.objects.annotate(
            num_comments_for_sorting=Count('comments')
        ).order_by('-num_comments_for_sorting', '-publication_date') # Спочатку за к-стю коментарів, потім за датою
        current_sorting = 'Кількістю коментарів'
    else: # За замовчуванням або якщо sort_by == 'date'
        articles_qs = Article.objects.order_by('-publication_date') # Новіші спочатку
        current_sorting = 'Датою публікації'

    for art in articles_qs: # ДІАГНОСТИКА
        print(f"Стаття: {art.title}, Дата: {art.publication_date}, Коментарів (властивість): {art.comment_count}") # ДІАГНОСТИКА
        if hasattr(art, 'num_comments_for_sorting'): # ДІАГНОСТИКА
            print(f"  Анотовано коментарів: {art.num_comments_for_sorting}") # ДІАГНОСТИКА
    print("-----------------------------") # ДІАГНОСТИКА

    context = {
        'articles': articles_qs,
        'current_sorting_param': sort_by, # Для підсвічування активного сортування
        'current_sorting_text': current_sorting,
        'page_title': "Список статей"
    }
    return render(request, 'blog/article_list.html', context)


# Залишаємо заглушки для інших функцій, які ми ще не реалізували
def article_detail(request, pk):
    # Це буде для детальної сторінки статті, реалізуємо пізніше
    pass

def comment_delete(request, pk):
    # Це буде для видалення коментаря, реалізуємо пізніше
    pass