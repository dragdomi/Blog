from django.urls import path
# from . import views
from .views import HomeView, PostDetailsView

urlpatterns = [
    # path('', views.home, name = "home"),
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailsView.as_view(), name="post_details")
]
