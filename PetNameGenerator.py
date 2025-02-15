import random

def pet_name_generator():
    adjectives = ["Happy", "Fluffy", "Bouncy", "Sparkly", "Silly"]
    animals = ["Puppy", "Kitten", "Bunny", "Hamster", "Turtle"]
    
    print(f"Your pet name could be: {random.choice(adjectives)} {random.choice(animals)} 🐾")
