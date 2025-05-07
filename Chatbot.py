def simple_chatbot():
    print("Hello! I’m your chatbot. Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input in ['hi', 'hello', 'hey']:
            print("Bot: Hello there! How can I assist you today?")
        
        elif "name" in user_input:
            print("Bot: I am a simple chatbot developed for an assignment!")
        
        elif "how are you" in user_input:
            print("Bot: I'm just code, but I'm running fine! 😊")
        
        elif "help" in user_input:
            print("Bot: I can answer simple questions like greetings, name, or how I'm doing.")
        
        elif "bye" in user_input or user_input == "exit":
            print("Bot: Goodbye! Have a great day! 👋")
            break
        
        else:
            print("Bot: I'm sorry, I didn't understand that. Try asking something else!")


simple_chatbot()
