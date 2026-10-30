 
def chatbot(): 
    print("Chatbot: Hello! I am a simple chatbot.") 
    print("Chatbot: Type 'bye' to exit.") 
 
    while True: 
        user_input = input("You: ").lower() 
 
        if "hello" in user_input or "hi" in user_input: 
            print("Chatbot: Hello! How can I help you?") 
 
        elif "how are you" in user_input: 
            print("Chatbot: I am fine. Thank you for asking!") 
 
        elif "your name" in user_input or "who are you" in user_input: 
            print("Chatbot: I am a rule-based chatbot.") 
 
        elif "help" in user_input: 
            print("Chatbot: I can answer simple predefined questions.") 
 
        elif "thank" in user_input: 
            print("Chatbot: You're welcome!") 
 
        elif "bye" in user_input or "exit" in user_input: 
            print("Chatbot: Goodbye! Have a nice day.") 
            break 
 
        else: 
            print("Chatbot: Sorry, I don't understand that.") 
 
 
chatbot() 