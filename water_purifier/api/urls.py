from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('employee/', views.EmployeeListCreateView.as_view(), name='employee'),
    path('employee/<uuid:pk>/', views.EmployeeRetrieveUpdateDestroyView.as_view(), name='employee_id'),
]
