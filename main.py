import openai

openai.api_key = 'API Key'
model="text-davinci-003"
prompt=input("enter text")

completion= openai.Completion.create(
  engine=model,
  prompt=prompt,  
  max_tokens=7,
  temperature=0,
    n=1,
    stop=None,
)

response=completion.choices[0].text
print(response)

