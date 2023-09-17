from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', views.admin_page, name='admin'),
    path('styled/', views.styled_page, name='styled'),
]