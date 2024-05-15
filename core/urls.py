from django.contrib import admin
from django.urls import path
from .views import handle_prompt


urlpatterns = [
    path('handle_prompt/',handle_prompt, name="handle_pormpt"),
]
