from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from employees.departments_app.models import Department
from employees.departments_app.serializers import DepartmentSerializer


class DepartmentListCreateView(ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    name = 'DEPARTMENTS'


class DepartmentUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    name = 'Department details'
