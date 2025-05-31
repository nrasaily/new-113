from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    
    
)
from .models import Post
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fiels = [
        "title", "subtitle" "body", "author"
    ]

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("list")  # list doesnot exist yet


    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "posts/create.html"
    fields = ["title", "subtitle", "body", "author", "status"]
    

class PostListView(ListView):
    template_name = "post/list.html"
    model = Post

class PostEditView(UpdateView):
    template_name = "posts/edit.html"
    fields = ["title", "subtitle", "body", "author", "status"]
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




