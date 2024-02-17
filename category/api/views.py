from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from account.models import User
from category.api.serializers import CategorySerializer, CategoryChatHistorySerializer
from category.api.utils import generate_response
from category.models import Category, ChatHistory
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


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

    def post(self, request, *args, **kwargs):
        prompt = request.data['prompt']

        category = request.data['category']
        previous_history = Category.objects.get(id=category).table
        category_name = Category.objects.get(id=category).name

        response = generate_response(category_name, previous_history, prompt)



        chat_history_data = {
            'category': request.data['category'],
            'prompt': prompt,
            'response': response,
        }

        try:
            if response['type'] == 'table':
                chat_history_data['summary_response'] = response['summary_response']
                category_instance = Category.objects.get(id=category)
                category_instance.table = str(response['updated_table_json_data'])
                category_instance.save()
        except:
            chat_history_data['error']: 'Could not save table'

        chat_history_serializer = CategoryChatHistorySerializer(data=chat_history_data)
        if chat_history_serializer.is_valid():
            chat_history_serializer.save()
        else:
            # Handle validation errors if needed
            pass

        return Response({
            'prompt': prompt,
            'response': response,
            'category': request.data['category'],
            'previous_history': previous_history,
            'updated_history': Category.objects.get(id=category).table
        })

    def patch(self, request, *args, **kwargs):
        try:
            request.data['user'] = User.objects.filter(uuid=request.data['user']).first().id
        except:
            pass
        return super().patch(request, *args, **kwargs)


class CategoryTableView:
    pass
