import nltk
import spacy
import random

nltk.download("punkt")
nlp = spacy.load("en_core_web_sm")

def get_named_entities(text):
    doc = nlp(text)
    return [ent.text for ent in doc.ents]

def simple_chatbot(user_input):
    user_input = user_input.lower()

    # Define some basic patterns and responses
    patterns = {
        "hello": ["Hi there!", "Hello!", "Hey!","Wassup"],
        "how are you": ["I am good, thank you!", "I\"m doing well. How about you?"],
        "bye": ["Goodbye!", "See you later!", "Bye!"],
        "name": ["Tannybot. You can call me Tannybot :)"],
        "named_entity": ["Tell me more about {}.", "I'm interested in {}.", "What is {}","What's the {}"],
    }

    # Check if any pattern matches the user input
    for pattern, responses in patterns.items():
        if pattern in user_input:
            if pattern == "named_entity":
                entities = get_named_entities(user_input)
                if entities:
                    return random.choice(responses).format(entities[0])
                else:
                    return "I didn't find any named entities."
            else:
                return random.choice(responses)

    # If no specific pattern matches, provide a default response
    return "Kya bol raha hai bhai? Can you please rephrase or ask a different question?"

def main():
    print("Chatbot: Hello! I'm a simple chatbot using NLTK and Spacy.")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        response = simple_chatbot(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
