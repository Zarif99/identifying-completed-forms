from django.urls import path

from .views import FormView

urlpatterns = [
    path('get/form/', FormView.as_view(), name='get_form'),
]
