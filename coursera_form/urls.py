from django.urls import path
from . import views
urlpatterns = [
    path('', views.SchemaView.as_view()),
]
