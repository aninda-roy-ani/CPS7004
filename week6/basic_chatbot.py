from nltk.chat.util import Chat, reflections


pairs = [
    (
        r"my name is (.*)",
        ["Hello %1, How are you today?", ]
    ),
    (
        r"what is your name?",
        ["My name is ChatBot and I'm here to help you.", ]
    ),
    (
        r"how are you?",
        ["I'm fine. What about you?", ]
    ),
    (
        r"i'm (.*) doing good",
        ["Nice to hear that", "Great", "Alright!"]
    ),
    (
        r"sorry (.*)",
        ["It's alright", "It's okay"]
    ),
    (
        r"quit",
        ["Goodbye. See you", "bye! Have a nice day!"]
    )
]

chatbot = Chat(pairs, reflections)


def chat():
    print("Hi! I'm a chatbot. Type quit to end the conversation")
    chatbot.converse()


chat()