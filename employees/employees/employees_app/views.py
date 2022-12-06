from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from employees.employees_app.models import Employee
from employees.employees_app.serializers import EmployeeSerializer


class EmployeeListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['id', 'username', ]
    search_fields = ['email', 'first_name', 'last_name', ]
    name = 'EMPLOYEES'


class EmployeeUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, ]

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    name = 'Employee details'
