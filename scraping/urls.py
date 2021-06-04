from django.urls import path
from . import views

urlpatterns = [
    path('', views.scraping_home, name='scraping_home'),
    path('scraping/<int:pk>/', views.scraping_detail, name='scraping_detail'),
    path('insta/', views.scraping_insta, name='scraping_insta'),
]
