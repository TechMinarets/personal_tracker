from django.urls import path
from .views import UserListView

urlpatterns = [
    path(
        route='users/',
        view=UserListView.as_view(),
        name='user-list'
    )
]
