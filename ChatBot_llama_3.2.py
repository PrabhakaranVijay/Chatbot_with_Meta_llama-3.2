# pip install huggingface_hub

# get api key from huggingface
# https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct

from huggingface_hub import InferenceClient
from apikey import huggingFaceApiKey2 as api_key

client = InferenceClient(api_key=api_key)

try:
    while True:
        user_input = input("You: ")

        # checking for exit condition (exit, bye, empty input)
        if (user_input.lower() == "exit" or 
            user_input.lower() == "bye" or 
            user_input.lower() == ""):
            break
        else:
            print("Bot: ", end="")
        
        # sending the input to the model
        # using meta llama 3.2 model
        for message in client.chat_completion(
            model="meta-llama/Llama-3.2-3B-Instruct",
            messages=[{
                "role": "user", 
                "content": user_input}],
            max_tokens=50,
            stream=True,
            temperature=0.5, # randomness
            ):
            
            print(message.choices[0].delta.content, end="")

except Exception as error:
    print("An error occurred:", str(error))

