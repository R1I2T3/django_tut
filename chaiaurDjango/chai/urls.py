from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home),
    path("<int:chai_id>/", views.chai_details, name="chai_details"),
    path("chai-stores/", views.chai_stores_view, name="chai-stores"),
]
