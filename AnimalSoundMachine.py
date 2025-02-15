def animal_sounds():
    print("Welcome to the Animal Sound Machine!")
    animals = {
        "dog": "Woof! 🐕",
        "cat": "Meow! 🐱",
        "cow": "Moo! 🐄",
        "duck": "Quack! 🦆"
    }
    
    animal = input("Choose an animal (dog/cat/cow/duck): ").lower()
    print(animals.get(animal, "I don't know that animal! 😕"))
