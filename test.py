# import google.generativeai as genai
from google.generativeai import GenerativeModel

API_KEY = 'AIzaSyBmpjwN8e1VxXXZWIIospFdrSnXh2mQPvQ'
# genai.configure(api_key=API_KEY)

model = GenerativeModel('gemini-pro-vision', )

prompt = 'Explain me more about the device in this image'

image_path = '/Users/avyuktsoni/Downloads/windmill.png'

with open(image_path, 'rb') as f:
    image_content = f.read()

response = model.generate_content(prompt)

print(response.text)