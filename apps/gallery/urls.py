from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("image/<int:id_>", views.image, name="image"),
    path("search/", views.search, name="search"),
    path("add-image/", views.add_image, name="add-image"),
    path("edit-image/<int:id_>", views.edit_image, name="edit-image"),
    path("delete-image/<int:id_>", views.delete_image, name="delete-image"),
    path("filtro/<str:category>", views.filter_category, name="filter-category"),

]
