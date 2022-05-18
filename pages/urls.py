from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomePageview.as_view(), name='home'),
    path('about/', views.AboutPageview.as_view(), name='about'),

]
