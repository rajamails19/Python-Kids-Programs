import random

def magic_8_ball():
    answers = ["Yes! ✅", "No! ❌", "Maybe! 🤔", 
               "Ask again later! ⏰", "Definitely! 💫"]
    
    input("Ask me a question: ")
    print(f"Magic 8 Ball says: {random.choice(answers)}")
