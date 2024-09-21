from django.urls import path
from blog.views import BlogListView
from blog.apps import BlogConfig

app_name = BlogConfig.name


urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list')


]