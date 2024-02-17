from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from category.api.serializers import CategorySerializer, CategoryChatHistorySerializer
from category.models import Category, ChatHistory
from rest_framework.permissions import AllowAny

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryMessageView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategoryChatHistorySerializer

    def get_object(self):
        return Category.objects.filter(id=self.kwargs['pk']).first().messages



class CategoryTableView:
    pass