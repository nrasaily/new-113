from django.views.generic import TemplateView
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

class PostListView(ListView):
    template_name = "posts/list.html"

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"

class PostUpdateView(UpdateView):
    template_name = "posts/update.html"

class PostCreateView(CreateView):
    template_name ="posts/create.html"

class PostDetailView(DetailView):
    template_name = "posts/detail.html"

