from django.urls import path
from . import views

app_name = 'blog'  # Важливо для простору імен URL

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('', views.article_list, name='article_list'),
     path('category/<int:category_pk>/articles/', views.article_list_by_category, name='article_list_by_category'),
    # path('article/<int:pk>/', views.article_detail, name='article_detail'),
    # path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
]