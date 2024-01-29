from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

from openai import OpenAI
client = OpenAI()
lesson = input("what topic are you teaching? ")
ability = input("what ability are the class? ")
length = input("how long is the lesson? ")
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "write the text for each slide of a powerpoint to teach a" + length + "lesson on" + lesson + "for" + ability + "ability secondary class"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)

from pptx import Presentation
from pptx.util import Inches
