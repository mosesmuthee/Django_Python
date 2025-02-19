from django.urls import path
from Alias1 import views

urlpatterns = [
    path('index/' ,views.index,name='my_home'),
]