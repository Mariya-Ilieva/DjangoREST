from django.urls import path

from employees.employees_app.views import EmployeeListCreateView, EmployeeUpdateDestroyView

urlpatterns = [
    path('', EmployeeListCreateView.as_view()),
    path('<int:pk>/', EmployeeUpdateDestroyView.as_view()),
]
