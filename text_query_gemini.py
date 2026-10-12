import base64
import mimetypes

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

image_path = 'ingredients.png'
mime_type, _ = mimetypes.guess_type(image_path)

with open(image_path, 'rb') as file:
    raw_binary = file.read()
    base64_bytes = base64.b64encode(raw_binary)
    image_base64 = base64_bytes.decode('utf-8')
    print(image_base64)

# Initialize the model
model = init_chat_model("gemini-3-flash-preview", model_provider="google_genai")

# Create message
message = [{"role": "user",
           "content":[{'type': 'text','text': 'Describe what you see in this image'},
                      {'type':'image', 'base64': image_base64, 'mime_type': mime_type}]
            }]

# Get and print the response
response = model.invoke(message)
print(response.text)