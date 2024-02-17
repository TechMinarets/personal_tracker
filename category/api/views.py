from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from account.models import User
from category.api.serializers import CategorySerializer, CategoryChatHistorySerializer
from category.models import Category, ChatHistory
from rest_framework.permissions import AllowAny

# import os
# from dotenv import load_dotenv
# # from google.generativeai import genai
# # load_dotenv()

# # genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# # model = genai.GenerativeModel('gemini-pro')

# import google.generativeai as genai
# import os
# from dotenv import load_dotenv
# from datetime import datetime
# load_dotenv()
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model = genai.GenerativeModel('gemini-pro')




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



class CategoryMessageView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategoryChatHistorySerializer

    def get_queryset(self, *args, **kwargs):
        return ChatHistory.objects.filter(category=self.kwargs['category_id'])
    
    def patch(self, request, *args, **kwargs):
        try:
            request.data['user'] = User.objects.filter(uuid=request.data['user']).first().id
        except:
            pass
        return super().patch(request, *args, **kwargs)
    
    



class CategoryTableView:
    pass