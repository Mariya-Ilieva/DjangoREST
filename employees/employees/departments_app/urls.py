from django.urls import path

from employees.departments_app.views import DepartmentListCreateView, DepartmentUpdateDestroyView

urlpatterns = [
    path('', DepartmentListCreateView.as_view()),
    path('<int:pk>/', DepartmentUpdateDestroyView.as_view()),
]
