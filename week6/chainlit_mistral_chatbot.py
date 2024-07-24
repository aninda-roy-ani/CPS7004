from mistralai.async_client import MistralAsyncClient
import chainlit as cl
from dotenv import load_dotenv
import os


load_dotenv()

client = MistralAsyncClient(api_key=os.environ.get("MISTRAL_API_KEY"))

# Initialize
cl.instrument_mistralai()

settings = {
    "model": "mistral-large-latest",
    "temperature": 0
}

@cl.on_message
async def on_message(message: cl.Message):
    res = await client.chat(
        messages=[
            {
                "content": "You may want to always reply in Bengali",
                "role": "system"
            },
            {
                "content": message.content,
                "role": "user"
            }
        ],
        **settings
    )
    await cl.Message(content=res.choices[0].message.content).send()