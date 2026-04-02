from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create_record),
    path('list/', get_records),
    path('update/<int:id>/', update_record),
    path('delete/<int:id>/', delete_record),
]