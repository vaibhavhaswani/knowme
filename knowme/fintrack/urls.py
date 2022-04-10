from django.urls import path
from .views import *

urlpatterns=[
path('expenses/',ExpenseView.as_view(),name='expense'),
path('expenses/eda/',EdaView.as_view(),name='expense_eda'),
]