# blog/urls.py
from django.urls import path

from .views import BlogListView

urlpatterns = [
    path('posts', BlogListView.as_view(), name='homework'),
#    path('homework/add-hw', add_hw, name = 'add_hw'),
]