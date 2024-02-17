from rest_framework.generics import ListAPIView

from account.api.serializers import UserSerializer
from account.models import User


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
