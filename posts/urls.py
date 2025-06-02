from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.PostCreateView.as_view(), name="create"),
    path("edit/", views.PostEditView.as_view(), name="edit"),
    path("delete/", views.PostDeleteView.as_view(), name="delete"),
    path("update/", views.PostUpdateView.as_view(), name="update"),
    path("list/", views.PostListView.as_view(), name="list"),
    path("detail", views.PostDetailView.as_view(), name="detail")
]