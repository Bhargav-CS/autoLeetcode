import google.generativeai as genai


from copy_text import copied_text

# read the api key from the file


welcome = """ hello people, welcome to the leetcode problem solver. I am here to help you solve the leetcode problems."""

with open("key.txt", "r") as f:
    api_key = f.read().strip()
    

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')



problem = copied_text
# print(problem)

response = model.generate_content(f"complete the leetcode problem and give optimized solution {problem} in python (code only)")
# print(response.text)

with open("solution.py", "w") as f:
    try:
        response = response.text.replace("```python", "").replace("```", "")
        f.write(response)
    except Exception as e:
        print(e)
        f.write("print('Hello World')")
    
print("Done")
    
    
