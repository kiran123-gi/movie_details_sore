from django.contrib import admin
from django.urls import path,include
from application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/',views.create_movies,name="create"),
    path('read/',views.read_movies,name='read'),
    path('update/<int:pk>/',views.update_movies,name = "update"),
    path('delete/<int:pk>/',views.delete_movies,name = "delete"),

    
]
