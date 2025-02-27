# -*- coding: utf-8 -*-
"""AIchatbot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SAF-TxL3DS37TWq3UqLGwRj0xGZrTQon

AI Chatbot project
Create a chatbot for dibimbing.id (a bootcamp school name)
Use Free API Key
This chatbot will use a free API Key from Google Gemini or OpenAI. Make sure you register and get the API Key needed to access the service.
Main Function of Chatbot
The chatbot you create must be able to:
1. Answer general questions about dibimbing.id that can be found on the page  
https://dibimbing.id/about-us
2. Display the types of bootcamp classes available, including a brief description and price of each class on the page
https://dibimbing.id/layanan/bootcamp
3. Register students for one of the bootcamp classes selected by the user.
4. Redirect students to the consultation link if the chatbot cannot answer the user's question.
5. Creating a Chatbot Interface
For the chatbot interface, create it using Streamlit so that it can interact with the chatbot visually.

Follow this tutorial to help understand how to use Function Calling with APIs from Google Gemini or OpenAI:
https://ai.google.dev/gemini-api/docs/function-calling/tutorial?lang=python
Tools
Google Collaboratory / Jupyter Notebook

POINTS:
Chatbot AI
- Using classes to chat with Gemini/OpenAI 25
- Using knowledge to answer questions 25
- Defining functions for class registration 15
- Defining functions to provide links to consultations 10
- Defining LLM classes to create responses + function calling 25
total :100

## Load environment variables
"""

# import os
# from google.colab import userdata
# import google.generativeai as genai


# genai.configure(api_key=userdata.get('GEMINI_API_KEY'))

import os
import google.generativeai as genai

# Fetch the API key from the environment variable
api_key = os.getenv('GEMINI_API_KEY')

if api_key:
    genai.configure(api_key=api_key)
else:
    print("API Key is not set")

"""## Answer General Questions About Dibimbing.id"""

# Knowledge Base
knowledge_base = {
    "mission": "Our mission is to help individuals and professionals develop skills for a successful career.",
    "vision": "Dibimbing.id aims to be the leading platform for career-focused bootcamps."
}

# Function to Answer General Questions
def get_general_info(prompt):
    for key, value in knowledge_base.items():
        if key in prompt.lower():
            return value
    return "Sorry, I don't have information about that."

# Test in Colab
user_query = "What is Dibimbing's mission?"
print(get_general_info(user_query))

"""## Test Bootcamp Classes Functionality"""

# Bootcamp Data
bootcamps = {
    "Data Science Bootcamp": {
        "description": "Learn foundational and advanced data science skills.",
        "price": "IDR 3,000,000"
    },
    "AI/ML Bootcamp": {
        "description": "Explore machine learning and AI model development.",
        "price": "IDR 4,500,000"
    }
}

# Function to Display Bootcamps
def get_bootcamp_info():
    response = "Here are the available bootcamp classes:\n"
    for bootcamp, details in bootcamps.items():
        response += f"- {bootcamp}: {details['description']} (Price: {details['price']})\n"
    return response

# Test in Colab
print(get_bootcamp_info())

"""## Test Registration Functionality"""

# Function to Register Students
def register_student(student_name, selected_bootcamp):
    if selected_bootcamp not in bootcamps:
        return "Sorry, the selected bootcamp is not available."
    return f"Student {student_name} has been successfully registered for the {selected_bootcamp}!"

# Test in Colab
student_name = "Fia"
selected_bootcamp = "Data Science Bootcamp"
print(register_student(student_name, selected_bootcamp))

# Test for invalid input
selected_bootcamp = "Nonexistent Bootcamp"
print(register_student(student_name, selected_bootcamp))

"""## Test Fallback to Consultation Link"""

# Fallback Consultation Link
consultation_link = "https://dibimbing.id/konsultasi"

# Function to Handle Fallbacks
def handle_fallback():
    return f"Sorry, I couldn't answer your question. Please visit our consultation page: {consultation_link}"

# Test in Colab
print(handle_fallback())

"""## Integrate LLM for Complex Queries"""

# Function to Handle Complex Queries
def chatbot_response(user_input):
    general_info = get_general_info(user_input)
    if general_info:
        return general_info
    elif "bootcamp" in user_input.lower():
        return get_bootcamp_info()
    else:
        # Fallback to Gemini API
        try:
            response = genai.chat(
                model="chat-bison-001",
                messages=[{"content": user_input, "author": "user"}]
            )
            return response['messages'][-1]['content']
        except Exception as e:
            print(f"Error: {e}")
            return handle_fallback()

# Test in Colab
print(chatbot_response("Tell me about Dibimbing's bootcamps."))
print(chatbot_response("How can I improve my career?"))  # Complex query to test LLM

"""## Build and Test Streamlit Interface"""

# Simulate Streamlit Interaction in Colab
user_input = "What is Dibimbing's vision?"
response = chatbot_response(user_input)
print(f"User: {user_input}")
print(f"Bot: {response}")

user_input = "Register me for AI/ML Bootcamp"
response = chatbot_response(user_input)
print(f"User: {user_input}")
print(f"Bot: {response}")

