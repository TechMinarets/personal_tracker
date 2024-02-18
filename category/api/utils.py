import json
import os
import pytz

from django.utils import timezone

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def response_to_json(response_text):
    return json.loads(response_text)


def generate_response(category_name, previous_history, prompt):
    openai_api_key = os.getenv('OPENAI_API_KEY')
    openai_model = os.getenv('OPENAI_MODEL')

    client = OpenAI(api_key=openai_api_key)

    # Set the timezone to Bangladesh
    bangladesh_timezone = pytz.timezone('Asia/Dhaka')

    # Get the current date and time in Bangladesh timezone
    current_date_month_year_time = timezone.now().astimezone(bangladesh_timezone).strftime('%Y-%m-%d %H:%M:%S')


    questions = [
        {
            'role': 'system',
            'content': f"Category: {category_name}\nPrevious History: {previous_history}"
        },
        {
            'role': 'system',
            'content': "If no previous history, the user is new. You can start from scratch and understand the context from the prompt and category name."
        },
        {
            'role': 'system',
            'content': f"Today is {current_date_month_year_time} in Bangladesh timezone."
        },
        {
            'role': 'user',
            'content': f"User's Prompt:\n{prompt}"
        },
        {
            'role': 'system',
            'content': """
User is in Bangladesh and may talk in Bengali but in English letters.
If the user wants information from previous history, reply in JSON format: { "type": "gk", "response": "your_response" }
If it's about modifying the table, provide updated table in JSON format: { "type": "table", "updated_table_json_data": {}, "summary_response": "summarize_your_response" }
If the user is not referring to history/table, reply in JSON format: { "type": "general", "response": "your_response" }

For updating the table, provide the updated table in the JSON format:
{
    "type": "table",
    "updated_table_json_data": {
        "columns": [...],
        "data": [
            [...],
            [...]
        ]
    },
    "summary_response": "..."
}
"""
        },
        {
            'role': 'system',
            'content': "Return a JSON as commanded. No need to explain when returning a table."
        }
    ]

    response = client.chat.completions.create(model='gpt-4', messages=questions)


    print(response.choices[0].message.content)

    try:
        return response_to_json(response.choices[0].message.content)
    except:
        pass

    return response.choices[0].message.content


def analyze_table_total_expenses(table_json):
    openai_api_key = os.getenv('OPENAI_API_KEY')
    openai_model = os.getenv('OPENAI_MODEL')

    client = OpenAI(api_key=openai_api_key)

    questions = [
        {
            'role': 'system',
            'content': f"Previous history/table JSON:\n{table_json}"
        },
        {
            'role': 'system',
            'content': "The user wants to know the total expenses from the table/history if exists. the default monetary unit is Taka (BDT)"
        }
    ]

    response = client.chat.completions.create(model='gpt-4', messages=questions)

    return response.choices[0].message.content

