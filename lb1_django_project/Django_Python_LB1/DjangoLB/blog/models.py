from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse # Додано для get_absolute_url
from django.db.models import Count # Додано для агрегації

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Назва категорії")

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Повертає URL для списку статей цієї категорії (створимо пізніше)
        return reverse('blog:article_list_by_category', args=[self.pk])


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Зміст")
    publication_date = models.DateTimeField(default=timezone.now, verbose_name="Дата публікації")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles', verbose_name="Категорія")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Автор")

    class Meta:
        verbose_name = "Стаття"
        verbose_name_plural = "Статті"
        ordering = ['-publication_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Повертає URL для перегляду цієї статті (створимо пізніше)
        return reverse('blog:article_detail', args=[self.pk])

    @property
    def comment_count(self):
        return self.comments.count()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name="Стаття")
    author_name = models.CharField(max_length=100, verbose_name="Ім'я автора")
    content = models.TextField(verbose_name="Текст коментаря")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата створення")

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"
        ordering = ['created_at']

    def __str__(self):
        return f"Коментар від {self.author_name} до статті '{self.article.title}'"

    def get_delete_url(self):
        # Повертає URL для видалення цього коментаря (створимо пізніше)
        return reverse('blog:comment_delete', args=[self.pk])