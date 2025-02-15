def emoji_story():
    print("Let's create an emoji story!")
    name = input("Enter a character name: ")
    place = input("Enter a place: ")
    action = input("Enter an action: ")
    
    story = f"""
    Once upon a time, {name} 👤
    Went to the {place} 🏠
    And started to {action} ⭐
    The End! 🎉
    """
    print(story)
