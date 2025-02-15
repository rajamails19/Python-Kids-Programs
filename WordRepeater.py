def word_repeater():
    word = input("Enter a word: ")
    times = int(input("How many times should I repeat it? "))
    
    for i in range(times):
        print(f"{i+1}. {word} ✨")
