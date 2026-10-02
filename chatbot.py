def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hello! How can I help you?"

    elif user_input == "how are you":
        return "I'm doing great! Thank you for asking."

    elif user_input == "what is your name":
        return "I'm a simple Python chatbot."

    elif user_input == "what can you do":
        return "I can respond to simple messages and answer basic questions."

    elif user_input == "thank you":
        return "You're welcome!"

    elif user_input == "good morning":
        return "Good morning! Have a great day."

    elif user_input == "good night":
        return "Good night! Sleep well."

    elif user_input == "bye":
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that."


print("Basic Chatbot")
print("----------------")
print("Type 'bye' to exit the chatbot.")
print()

while True:
    user_input = input("You: ")

    response = chatbot_response(user_input)

    print("Bot:", response)

    if user_input.lower() == "bye":
        break