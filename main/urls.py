from django.urls import path
from .views import(
    UserView,
    AreasView,
    CreaeteAreaView,
    GetAreaView,
    UpdateAreaView,
    DeleteAreaView
)


urlpatterns = [
    path('users/', UserView.as_view()),
    path('areas', AreasView.as_view()),
    path('create_area/', CreaeteAreaView.as_view()),
    path('area/<int:pk>/', GetAreaView.as_view()),
    path('update_area/<int:pk>/', UpdateAreaView.as_view()),
    path('delete_area/<int:pk>/', DeleteAreaView.as_view()),
]