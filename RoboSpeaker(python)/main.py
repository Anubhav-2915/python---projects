import os

print("Welcome to RoboSpeaker!!")

while True:
    x = input("Enter what you want the RoboSpeaker to speak: ")
    if x == 'z':
        y = "Thank You"
        os.system(f"say {y} ")
        break

    command = f"say {x}"
    os.system(command)

