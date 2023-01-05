import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_FLIRT = "Bruh, i was made by Jeet, he dosnt know how to do that that!, you dumbass,i'm sorry."


def unknown():
    response = ["Could you please re-phrase that? ",
                "Please like say it again, i dont know what you are saying, google failed me"][
        random.randrange(2)]
    return response