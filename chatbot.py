def chatbot():
  while True:
    user_input = input("You: ")
    user_input = user_input.lower()  # Convert input to lowercase for easier matching

    # Greeting
    if user_input in ("hi", "hello", "hey"):
      print("Chatbot: Hi there! How can I help you today?")

    # Answering a question
    elif "what is your name" in user_input:
      print("Chatbot: My name is cb, a friendly chatbot!")

    # Responding to goodbye
    elif user_input in ("bye", "goodbye", "see you later"):
      print("Chatbot: Bye! Have a great day.")
      break

    # Default response
    else:
      print("Chatbot: Sorry, I can't understand that yet. Try asking a different question!")

if _name_ == "_main_":
  chatbot()
