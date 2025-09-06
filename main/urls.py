from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("calculate/", views.calculate, name="calculate"),
    path("analysis/", views.analysis, name="analysis")
]
