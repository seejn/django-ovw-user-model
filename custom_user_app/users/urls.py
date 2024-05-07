from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), # ROUTE FOR GET, POST
    path('<int:user_id>/', views.index, name="userid_index"), # ROUTE FOR GET, PUT, PATCH, DELETE
]