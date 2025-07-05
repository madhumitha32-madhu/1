def chatbot():
    print("chatbot: Hello! Have a good day! What can I help with?")
    while True:
        user_input=input("Madhu:").lower()
        if "hello" in user_input or "hi" in user_input:
            print("chatbot: Hello! what did you need I'm ready to help you")
        elif "product" in user_input:
            print("chatbot: things, Jewel, cosmetic")
        elif "things" in user_input:
            print("chatbot: What price do you want?")
        elif "price" in user_input:
            print("chatbot: What price are you expecting?")
        elif "500" in user_input or "1000" in user_input:
            print("chatbot: Things are available")
        elif "byee" in user_input:
            print("chatbot: Sure,Bye!")
            break
        else:
            print("chatbot: If you need any other resources I'm here to help You")
                                    
                                    
if __name__=="__main__":
  chatbot()
            
