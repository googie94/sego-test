from django.urls import path
from . import views


app_name='okr'
urlpatterns = [
	path('', views.OkrView, name='okrview'),
]