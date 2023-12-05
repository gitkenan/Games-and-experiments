# Function to respond to different types of user input
def respond(input_text):
    if "hello" in input_text.lower():
        return "Hello! How can I help you?"
    elif "bye" in input_text.lower():
        return "Goodbye! Have a great day!"
    elif "how are you" in input_text.lower():
        return "I'm just a computer program, but I'm doing well, thank you!"
    elif "thanks" in input_text.lower() or "thank you" in input_text.lower():
        return "You're welcome!"
    else:
        return "I'm not sure how to respond to that."

# Main loop to run the chatbot
def main():
    print("AI Chatbot: Hello! Ask me something or say goodbye to exit.")
    while True:
        user_input = input("You: ")
        response = respond(user_input)
        print("AI Chatbot:", response)
        if "bye" in user_input.lower():
            break

if __name__ == "__main__":
    main()

