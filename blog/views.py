from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Blog_Entry
from urllib import request

class BlogListView(ListView):
    model = Blog_Entry

class BlogDetailView(DetailView):
    model = Blog_Entry

    def get_object(self, queryset=None):
        self.object=super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog_Entry
    fields = ("title", "slug", "content", "preview", "creation_date","is_published")
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(UpdateView):
    model = Blog_Entry
    fields = ("title", "slug", "content", "preview", "creation_date","is_published")
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse('blog:blog_entry', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog_Entry
    success_url = reverse_lazy('blog:blog_list')

def Subscribe(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"You have new message from {name}({email}): {message}")
    return render(request, "blog/blog_subscribe.html")