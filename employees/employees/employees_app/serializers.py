from rest_framework.serializers import ModelSerializer
from employees.employees_app.models import Employee


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        exclude = ['password', ]


class DetailEmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
