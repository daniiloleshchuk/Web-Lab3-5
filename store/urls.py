from django.conf.urls.static import static
from django.urls import path

from web import settings
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create', views.create_page, name="create"),
    path('edit/<int:id>', views.edit_page, name="edit"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('<search_query>', views.index, name="index_search"),
]

