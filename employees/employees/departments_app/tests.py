from django.test import TestCase
from employees.departments_app.models import Department


class DepartmentTest(TestCase):
    def setUp(self):
        self.dep1 = Department.objects.create(title='IT', category='C2')

    def test_department_created_success(self):
        self.assertEqual(self.dep1.title, 'IT')
        self.assertEqual(self.dep1.category, 'C2')
