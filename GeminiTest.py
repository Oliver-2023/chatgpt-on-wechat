import pathlib
import textwrap
import time

import google.generativeai as genai

from IPython.display import Markdown


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key="AIzaSyDb0CIsEsNrOCOVjKQ4Dj2atn4-VTVm9t4",transport='rest')

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

time1 = time.time()
model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("朝花夕拾是谁在什么时候写的，当时他的处境如何")
time2 =time.time()
time_cut =time2-time1
print(time_cut)
to_markdown(response.text)

print(response.text)