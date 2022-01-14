from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path('', views.show_list, name="list"),
    path('order_by_<int:pk>/', views.show_ordered_list, name="ordered_list"),
    path('write/', views.write_review, name="write"),
    path('<int:pk>/', views.show_detail, name="detail"),
    path('update/<int:pk>/', views.update_review, name="update"),
    path('delete/<int:pk>/', views.delete_review, name="delete")
]