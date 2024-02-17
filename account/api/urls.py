from django.urls import path
from .views import UserListView, UserCategoryListView

urlpatterns = [
    path(
        route='users/',
        view=UserListView.as_view(),
        name='user-list'
    ),
    path(
        route='user/<uuid>/categories/',
        view=UserCategoryListView.as_view(),
        name='category-detail'
    )
]




















































































