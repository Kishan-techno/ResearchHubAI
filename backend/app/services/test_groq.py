from groq import Groq

client = Groq(api_key="PASTE_YOUR_KEY_HERE")

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "Hello"}
    ],
    model="llama3-70b-8192",
)

print(chat_completion.choices[0].message.content)