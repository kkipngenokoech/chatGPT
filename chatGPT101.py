import openai

api_key = "paste your api key here"

openai.api_key = api_key

prompt = "Give me a list of the 7 wonders of the world"

def getResponse(prompt, model = "gpt-3.5-turbo",temperature=0, max_tokens=500):
    response = openai.ChatCompletion.create(model = model, messages = prompt, temperature = temperature, max_tokens = max_tokens)
    
    return response.choices[0].message['content']

response = getResponse(prompt=prompt)
print(response)