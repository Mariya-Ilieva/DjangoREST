from rest_framework.serializers import ModelSerializer

from employees.departments_app.models import Department


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
