def draw_shape():
    shape = input("What shape should I draw? (square/triangle): ").lower()
    
    if shape == "square":
        print("⬜ Here's your square:")
        for _ in range(4):
            print("* * * *")
    elif shape == "triangle":
        print("📐 Here's your triangle:")
        for i in range(1, 5):
            print("* " * i)
