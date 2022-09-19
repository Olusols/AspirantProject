from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('aggregate-predictor/', views.aggregate_predictor, name='aggregate-predictor'),
    path('subject-checker/', views.subject_checker, name='subject-checker'),
    path('cutoff-tracker/', views.cutoff_tracker, name='cutoff-tracker'),
    path('chance-calculator/', views.chance_calculator, name='chance-calculator'),
    
]