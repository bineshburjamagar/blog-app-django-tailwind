from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
     path('', views.BlogPage.as_view(), name = 'blogpage'),
     path('<slug:slug>/', views.BlogDetails.as_view(), name= 'blog-details' )
    
]