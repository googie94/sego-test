from django.urls import path
from . import views

urlpatterns = [
    path('', views.scraping_home, name='scraping_home'),
    path('<str:post_id>/', views.scraping_detail, name='scraping_detail'),
    path('insta/', views.scraping_insta, name='scraping_insta'),
]
