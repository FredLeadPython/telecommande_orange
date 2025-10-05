from django.urls import path
from . import views

app_name = 'telecommande'

urlpatterns = [
    path('', views.remote_control_view, name='remote'),
    path('send_command/', views.send_command_view, name='send_command'),
]
