import time

def rule_based_chatbot():
    print("Chatbot: Hello! I am a rule-based AI assistant. How can I help you today?")
    print("(Type 'exit', 'bye', or 'quit' to stop the conversation)\n")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        # Rule 1: Exit condition
        if user_input in ['exit', 'bye', 'quit']:
            print("Chatbot: Goodbye! Have a wonderful day!")
            break
            
        # Rule 2: Greetings
        elif any(word in user_input for word in ['hello', 'hi', 'hey', 'sup']):
            print("Chatbot: Hello there! Hope you are doing well. How can I assist you?")
            
        # Rule 3: Identity/Name
        elif 'your name' in user_input or 'who are you' in user_input:
            print("Chatbot: I am a simple rule-based chatbot created for my CodSoft internship!")
            
        # Rule 4: How are you
        elif 'how are you' in user_input or 'how is it going' in user_input:
            print("Chatbot: I don't have feelings, but my code is running perfectly! Thanks for asking.")
            
        # Rule 5: Help/Capabilities
        elif 'help' in user_input or 'what can you do' in user_input:
            print("Chatbot: I can answer basic greetings, tell you my name, or help you close this chat.")
            
        # Rule 6: Thank you
        elif 'thank you' in user_input or 'thanks' in user_input:
            print("Chatbot: You're very welcome! Let me know if you need anything else.")
            
        # Fallback rule: Unknown inputs
        else:
            print("Chatbot: I'm sorry, I don't quite understand that. Could you try phrasing it differently?")
            
        time.sleep(0.3)

if __name__ == "__main__":
    rule_based_chatbot()