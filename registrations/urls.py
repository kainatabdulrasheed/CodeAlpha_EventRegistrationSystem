from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_registration),
    path('my/', views.my_registrations),
    path('<int:pk>/cancel/', views.cancel_registration),
]