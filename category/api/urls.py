from django.urls import path

from category.api import views

urlpatterns = [
    path(
        route='categories/',
        view=views.CategoryListView.as_view(),
        name='category-list'
    ),
    path(
        route='<int:category_id>/chat-history',
        view=views.CategoryMessageView.as_view(),
        name='category-messages'
    ),
    # path(
    #     route='categories/<int:pk>/table-history',
    #     view=views.CategoryTableView.as_view(),
    #     name='category-table'
    # )
    path(
        route='categories/<int:pk>/',
        view=views.CategoryDetailView.as_view(),
        name='category-detail'
    )
]
