
class SMSA_Chatbot:
    def __init__(self):
        self.rules = {
            "hi": "Hello! how can I assist you today? \n 1. Farmer \n 2. Buyer \n 3. Expert \n 4. Exit",
            "1": "Welcome to the Farmer section.",
            "2": "Welcome to the Buyer section.",
            "3": "Welcome to the Expert section.",
            "4": "Thank you for using SMSA Chatbot.",
        }
    
    def respond(self, message):
        message = message.lower().strip()
        for pattern in self.rules:
            if pattern in message:
                return self.rules[pattern]
        return "I'm not sure how to respond to that. Try saying 'help'."
    
chatbot = SMSA_Chatbot()
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", chatbot.respond(user_input))
        
        