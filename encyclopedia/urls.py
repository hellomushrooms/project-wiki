from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("addpage/", views.addpage, name="addpage"),
    path("editpage/", views.editpage, name="editpage"),
    path("saveedit/", views.saveedit, name="saveedit"),
    path("random/", views.randomentry, name="randomentry")
]
