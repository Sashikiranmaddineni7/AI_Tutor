import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_response(prompt):
    try:
        # Create chat completion request
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3-8b-8192",
            temperature=1.2,
            max_tokens=500,
            top_p=0,
            stream=False,
            stop="exit"
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    print("Welcome to your AI Tutor. Ask me anything about machine learning!")
    while True:
        inp = input("You: ")
        if inp.lower() in ['exit', 'quit']:
            print("bye!")
            break
        response = generate_response(inp)
        print(f"AI Tutor: {response}")

if __name__ == "__main__":
    main()
