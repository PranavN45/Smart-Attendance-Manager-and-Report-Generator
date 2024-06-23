from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.clalogin, name='clalogin'),
    path('index/', views.clatrindex, name='clatrindex'),
    path('download_report/', views.down_report, name='down_report'),
]
