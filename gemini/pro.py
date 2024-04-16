import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["give me code for printing prime numbers from 1 to 100 in python"]
  },
  {
    "role": "model",
    "parts": ["```python\n# Function to check if a number is prime\ndef is_prime(num):\n    if num <= 1:\n        return False\n    for i in range(2, num):\n        if num % i == 0:\n            return False\n    return True\n\n# Print prime numbers from 1 to 100\nfor i in range(1, 101):\n    if is_prime(i):\n        print(i, end=\" \")\n```"]
  },
  {
    "role": "user",
    "parts": ["give me code for printing prime numbers from 1 to 100 in python"]
  },
  {
    "role": "model",
    "parts": ["Here is a simple Python program to print prime numbers from 1 to 100:\n\n```python\n# Function to check if a number is prime\ndef is_prime(num):\n    if num <= 1:\n        return False\n    for i in range(2, int(num**0.5) + 1):\n        if num % i == 0:\n            return False\n    return True\n\n# Print prime numbers from 1 to 100\nfor i in range(1, 101):\n    if is_prime(i):\n        print(i, end=\" \")\n```"]
  },
  {
    "role": "user",
    "parts": ["give me code for printing prime numbers from 1 to 100 in python"]
  },
  {
    "role": "model",
    "parts": ["Here is a simple Python program that will print all prime numbers from 1 to 100:\n\n```python\n# Function to check if a number is prime\ndef is_prime(n):\n    if n <= 1:\n        return False\n    for i in range(2, n):\n        if n % i == 0:\n            return False\n    return True\n\n# Print all prime numbers from 1 to 100\nfor i in range(1, 101):\n    if is_prime(i):\n        print(i, end=\" \")\n```"]
  },
])

convo.send_message("write an essay under 2000 words on generative AI")
print(convo.last.text)