from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newentry",views.newentry,name="newentry"),
    path("search",views.search,name="search"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("editpage/<str:title>",views.editpage,name="editpage"),
    path("editedpage/<str:title>",views.editedpage,name="editedpage"),
    path("random_entry",views.random_entry,name="random_entry")

    ]
