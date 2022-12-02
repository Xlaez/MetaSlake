from django.urls import path
from stake import views


urlpatterns = [
    path("chains/", views.ChainView.as_view()),
    path("stakes/", views.StakeView.as_view()),
    path("stakes/<slug:slug>", views.StakeUpdateView.as_view())
]