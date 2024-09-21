from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Blog_Entry


class BlogListView(ListView):
    model = Blog_Entry
