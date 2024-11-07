from nltk.chat.util import Chat, reflections

patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you\?', ["I am good, thank you!", "I'm doing fine, thanks!"]),
    (r'what is your name\?', ["My name is Chatbot."]),
    (r'bye|goodbye', ['Goodbye!', 'Bye!', 'Take care!']),
    (r'my name is (.*)', [r'Hello, %1!']),
    (r'(.*)(location|city)?', ["I'm a virtual being, so I don't have a location."]),
    (r'(.*) created you?', ['I was created by an awesome developer.']),
    (r'(.*)(weather|temperature|forecast)(.*)', ["I'm a chatbot, not a weather bot."])  # Adjusted pattern
]

def chatbot():
    print("Welcome! Type 'bye' to exit.")
    chatbot_instance = Chat(patterns, reflections)

    while True:
        user_input = input("You: ").lower()
        if user_input == 'bye':
            print("Chatbot: Goodbye!")
            break
        else:
            response = chatbot_instance.respond(user_input)
            print("Chatbot:", response if response else "I'm not sure how to respond to that.")

if __name__ == "__main__":
    chatbot()

# sudo apt install python3-pip
# pip install nltk 
# or
# pip3 install nltk
# TC:O(n)
# SC:O(n)
