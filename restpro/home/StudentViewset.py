from rest_framework import  viewsets
from .models import Student
from .StudentSerializer import StudentSerializer
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    parser_classes = (MultiPartParser, FormParser)
    
    