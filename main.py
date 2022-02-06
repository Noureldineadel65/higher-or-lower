from random import choice
from data import data
score = 0
continue_playing = True
print("""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/  
""")
while continue_playing:
    first_choice = choice(data)
    second_choice = choice(data)
    while True:
        print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}")
        print("""
         _    __    
        | |  / /____
        | | / / ___/
        | |/ (__  ) 
        |___/____(_)
        """)
        print(f"Against B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}")
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_choice == "a":
            if first_choice["follower_count"] >= second_choice["follower_count"]:
                score += 1
                print(f"You are right! Current score: {score}")
                second_choice = choice(data)
            else:
                print(f"That's wrong, Final score: {score}")
                break
        else:
            if first_choice["follower_count"] <= second_choice["follower_count"]:
                score += 1
                print(f"You are right! Current score: {score}")
                first_choice = choice(data)
            else:
                print(f"That's wrong, Final score: {score}")
                break
    if input("Do you want to try again? Type 'y' for yes or 'n' for no: ").lower() == 'n':
        continue_playing = False
