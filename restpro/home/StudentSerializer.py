from rest_framework import routers, serializers
from .models import Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'