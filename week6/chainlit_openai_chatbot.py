from openai import OpenAI
import chainlit as cl
from chainlit import (AskUserMessage,
                      Message,
                      on_chat_start)
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


async def ask_openai(prompt):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[{
            "role": "system", "content": "You respond in Bengali"
        },{
            "role": "user", "content": prompt
        }]
    )
    return response.choices[0].message.content.strip()


@on_chat_start
async def start_conversation():
    res = await AskUserMessage(content="What is your name?",
                               timeout=30).send()
    if res:
        llm_response = await ask_openai(f"Hello {res['output']}")
        await Message(content=llm_response).send()


@cl.on_message
async def on_message( message : cl.Message ):
    llm_response = await ask_openai(message.content)
    await Message(content=llm_response).send()