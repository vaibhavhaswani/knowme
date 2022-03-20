from django.urls import path
from .views import *

urlpatterns=[
path('expenses/',ExpenseView.as_view(),name='expense') 
]