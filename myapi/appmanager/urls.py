from django.urls import path
from . import views

urlpatterns = [
    path('add-app', views.add_app, name='add-app'),
    path('get-app/<int:id>', views.get_app, name='get-app'),
    path('delete-app/<int:id>', views.delete_app, name='delete-app'),
]
