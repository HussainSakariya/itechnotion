from django.urls import path
from .views import *

urlpatterns = [
    path('',index.as_view(),name="index"),
    path('insert/',InsertData.as_view(),name="insert"),
    path('update/<int:pk>/',UpdateData.as_view(),name="update"),
    path('delete/<int:pk>/',DeleteData.as_view(),name="delete"),
]