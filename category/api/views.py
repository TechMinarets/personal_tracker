from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from account.models import User
from category.api.serializers import CategorySerializer, CategoryChatHistorySerializer
from category.models import Category, ChatHistory
from rest_framework.permissions import AllowAny

class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def post(self, request, *args, **kwargs):
        try:
            request.data['user'] = User.objects.filter(uuid=request.data['user']).first().id
        except:
            pass
        return super().post(request, *args, **kwargs)

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class CategoryMessageView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategoryChatHistorySerializer

    def get_object(self):
        return Category.objects.filter(id=self.kwargs['pk']).first().messages
    
    def patch(self, request, *args, **kwargs):
        try:
            request.data['user'] = User.objects.filter(uuid=request.data['user']).first().id
        except:
            pass
        return super().patch(request, *args, **kwargs)
    
    



class CategoryTableView:
    pass