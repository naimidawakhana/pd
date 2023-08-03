from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name= 'index'),
    path('', views.login_view, name='login_view'),
    # path('', views.index, name= 'index'),
    # path('', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    # path('adminpage/', views.admin, name='adminpage'),
    # path('customer/', views.customer, name='customer'),
    # path('employee/', views.employee, name='employee'),
    path('booking/', include('booking.urls')),
]