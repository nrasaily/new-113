from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Status
from .models import Post
from django.urls import reverse_lazy, reverse

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

    success_url = reverse_lazy("list")  # list doesnot exist yet

    #def get_success_url(self):
     #   return reverse('list')
    

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        published = Status.objects.get(name="published")
        context["title"] = "Published"
        context["post_list"] = (
            Post.objects
            .filter(status=published)
            .order_by("created_on").reverse()
        )
        return context

class ArchivedPostListView(LoginRequiredMixin, ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwrgs):
        context = super().get_context_data(**kwrgs)
        archived = Status.objects.get(name="archived")
        context["title"] = "Archived"
        context["post_list"] = (
            Post.objects
            .filter(status=archived)
            .order_by("created_on").reverse()
        )
        return context

class DraftPostListView(LoginRequiredMixin, ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft = Status.objects.get(name="draft")
        context["title"] = "Draft"
        context["post_list"] = (
            Post.objects
            .filter(status=draft)
            .filter(author=self.request.user)
            .order_by("created_on").reverse()
        )
        return context

class PostEditView(UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"
    fields = ["title", "subtitle", "body", "author", "status"]
    model = Post

    def test_func(self):
        post = self.get_object()
        if post.status.name == "published":
            return True
        elif post.status.name == "archived" and self.request.user.is_authenticated:
            return True
        else:
            return False


class PostDetailView(UserPassesTestMixin, DetailView):
    template_name = "posts/detail.html"
    model = Post

    def test_func(self):
        Post = self.get_object()
        if post.status.name == "published":
            return True 
        elif post.status.name == "archieved" and self.request.user.is_authenticated:
            return True
        elif post.status.name == "drafts" and self.request.user == post.author:
            return True
        else:
            return False


