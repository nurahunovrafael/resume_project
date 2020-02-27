from django.urls import path
from .views import ResumeFormView

urlpatterns = [
    path('resume/', ResumeFormView.as_view(), name='resume'),
]