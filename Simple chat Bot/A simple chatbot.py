import datetime
import random
jokes = [
    "Why don’t skeletons fight each other? They don’t have the guts!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the computer go to the doctor? Because it caught a virus!",
    "Why did the math book look sad? Because it had too many problems."
]

print("Hello! I'm ChatBot 🤖. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if any(greet in user_input for greet in ["hi", "hello", "hey"]):
        print("Bot: Hello there! How can I help you?")
    elif "your name" in user_input:
        print("Bot: I'm ChatBot, your virtual assistant.")
    elif "how are you" in user_input:
        print("Bot: I'm doing great, thanks for asking! How about you?")
    elif "weather" in user_input:
        print("Bot: I can't check the weather right now, but I hope it's nice where you are.")
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(f"Bot: The current time is {current_time}.")
    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        print(f"Bot: Today's date is {current_date}.")
    elif "joke" in user_input:
        print("Bot:", random.choice(jokes))
    elif "bye" in user_input:
        print("Bot: Goodbye! Have a great day. 👋")
        break
    else:
        print("Bot: Sorry, I don't understand. Can you rephrase?")
