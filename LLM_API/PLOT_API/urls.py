

from django.urls import path
from .views import generate_plot

urlpatterns = [
    path('generate-plot/', generate_plot, name='generate-plot'),  # URL specific to the newsplot app
]
