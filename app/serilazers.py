from rest_framework.serializers import ModelSerializer
from app.models import Category


class CategoryListAPIView(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name'
        ]
