from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create_user),
    path('list/', list_users),
    path('update/<int:id>/', update_user),
    path('delete/<int:id>/', delete_user),
    
]