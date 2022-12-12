from django.shortcuts import render
from .serilazers import CategoryListAPIView
from rest_framework.generics import ListAPIView
from app.models import Category


# Create your views here.
class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListAPIView
