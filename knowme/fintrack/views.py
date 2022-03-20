from urllib import request
# from django import views
from django.shortcuts import render

# Create your views here.
from .serializers import ExpenseSerializer
from rest_framework import status,views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Expense


class ExpenseView(views.APIView):  #The viewsets base class provides the implementation for CRUD operations by default
    # serializer_class=ExpenseSerializer
    # queryset=Expense.objects.all()
    def post(self,request):
        serializer=ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        expenses=Expense.objects.all()
        expense_data=ExpenseSerializer(expenses,many=True)
        return Response(expense_data.data)
