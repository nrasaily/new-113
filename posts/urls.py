from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("drafts/", views.DraftPostListView.as_view(), name="drafts"),
    path("archive/", views.ArchivedPostListView.as_view(), name="archive"),
    path("new/", views.PostCreateView.as_view(), name="new"),
    path("<int:pk>/detail", views.PostDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.PostEditView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete"),
    path("update/", views.PostUpdateView.as_view(), name="update"),
]