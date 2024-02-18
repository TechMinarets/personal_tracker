import json

from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from account.models import User
from category.api.serializers import CategorySerializer, CategoryChatHistorySerializer
from category.api.utils import generate_response, analyze_table_total_expenses
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
            user = User.objects.get(uuid=request.data['user'])
            category = Category(name=request.data['name'], user=user)
            category.save()
        except Exception as e:
            print(e)
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
            'response': str(response),
        }

        try:
            if 'response' in response:
                chat_history_data['response'] = response['response']
        except:
            pass

        try:
            if response['type'] == 'table':
                if 'summary_response' in response:
                    chat_history_data['response'] = response['summary_response']

                category_instance = Category.objects.get(id=category)
                category_instance.table = str(response['updated_table_json_data'])
                category_instance.save()
        except:
            chat_history_data['error']: 'Could not save table'

        chat_history_data
        chat_history_serializer = CategoryChatHistorySerializer(data=chat_history_data)
        if chat_history_serializer.is_valid():
            chat_history_serializer.save()
        else:
            # Handle validation errors if needed
            pass

        return Response(chat_history_data)

    def patch(self, request, *args, **kwargs):
        try:
            request.data['user'] = User.objects.filter(uuid=request.data['user']).first().id
        except:
            pass
        return super().patch(request, *args, **kwargs)


def response_to_json(response_text):
    return json.loads(response_text)


class CategoryTableView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        table = Category.objects.filter(id=self.kwargs['pk']).first().table
        table_json = table.replace("'", "\"")

        total_expenses = analyze_table_total_expenses(table_json)

        return Response(
            {
                'table': response_to_json(table_json),
                'total_expenses': total_expenses
            }

        )
