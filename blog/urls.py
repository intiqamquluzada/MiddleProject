from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_list_view, name='list')
]
