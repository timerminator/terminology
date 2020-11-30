from django.urls import path
from .views import HandbookView, ElementsHandbookView, ValidateElementsHandbookView

urlpatterns = [
    path('handbooks/', HandbookView.as_view()),
    path('elements_handbook/', ElementsHandbookView.as_view()),
    path('validate_elements_handbook/', ValidateElementsHandbookView.as_view())
]