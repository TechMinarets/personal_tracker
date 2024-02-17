from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from account.api.serializers import UserSerializer
from account.models import User
from category.api.serializers import CategorySerializer
from category.models import Category
from .serializers import UserCategorySerializer


class UserListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        print(request.user)
        return self.create(request, *args, **kwargs)

class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Compare this snippet from account/api/views.py:
class UserCategoryListView(ListAPIView):
    serializer_class = CategorySerializer  # Use the modified serializer
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Category.objects.filter(user__uuid=kwargs['uuid'])


        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return super().get(request, *args, **kwargs)






# Compare
    

