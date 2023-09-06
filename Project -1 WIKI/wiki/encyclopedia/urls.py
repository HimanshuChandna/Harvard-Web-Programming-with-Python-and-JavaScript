from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("md_to_html", views.md_to_html, name="md_to_html"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("create_new_page", views.create_new_page, name='create_new_page'),
    path("random_page", views.random_page, name='random_page'),
    path("query", views.query, name='query'),
    path("edit_page", views.edit_page, name='edit_page')

]
