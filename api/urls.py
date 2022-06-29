from django.urls import path
from .views.electronics import ElectronicsView, ElectronicView


urlpatterns = [
    path('electronics/', ElectronicsView.as_view(), name='index'),
    path('electronics/<int:pk>', ElectronicView.as_view(), name='electronic')
]