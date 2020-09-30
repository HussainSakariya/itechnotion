from django.urls import path
from .views import *

urlpatterns = [
    path('',index.as_view(),name="index"),
    path('insert/',InsertData.as_view(),name="insert"),
]