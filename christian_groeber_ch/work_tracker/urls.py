from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('create/', views.new_project),
    path('start-working/<project_id>/', views.start_working),
]