import google.generativeai as genai
import os

# read the api key from the file
with open("key.txt", "r") as f:
    api_key = f.read().strip()
    

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

problem = "88. Merge Sorted Array"

response = model.generate_content(f"write a solution for the leetcode problem: {problem} in python (code only)")
print(response.text)

with open("solution.py", "w") as f:
    txt = response.text.replace("```python", "").replace("```", "")
    f.write(txt)
    
