from django.urls import path
from . import views

app_name = 'jornalOnline'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article/<int:article_id>/add-comment/', views.add_comment, name='add_comment'),
    path('article/<int:article_id>/add-rating/', views.add_rating, name='add_rating'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('article/add/', views.add_article, name='add_article'),


]
