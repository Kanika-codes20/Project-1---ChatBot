# This is a simple Chat Bot
# Welcome the user

print("Welcome to the ChatBOT BananaMilkshake❤")

username = input("What is your name?")

# Have the ChatBot greet the user by name
print("Nice to meet you, " + username + "!")
print("That's a lovely name!")

# Adding random
import random

positive = ["i'm good!", "good!", "good", "great", "i'm doing good", "great!", "awesome", "never felt better",
            "better than ever", "i'm good!", "i'm good", "i'm doing great!"]
neutral = ["okay", "fine", "alright", "i'm doing fine", "i'm doing alright", "i'm doing quite fine"]
negative = ["bad", "not good", "i'm not feeling good", "i'm not okay", "i'm tired", "not fine"]


# Making list of positive, neutral, negative and fallback replies
positive_replies = [
    "That's great, keep having fun!",
    "Yes, I'm happy for you!",
    "Niceeee, keep going...!",
]

neutral_replies = [
    "Uh huh, I totally get it! Some days are just meant to be a lil boring. (♪´▽｀)",
    "I see! How 'bout a cup of coffee to make your day better? :>",
    "So proud of you for surviving another day!(`*>﹏<*′)",
]

negative_replies = [
    "That sounds rough.",
    "Oh, take care!",
    "Sad to hear that!.",
]

fallback_replies = [
    "I see. Thank you for sharing!",
    "Is that so?",
    "Cool. :O"
]

# Add a loop first

while True:
    print("\n")

    feeling = input("How are you doing?")

    # Turning into lowercase and getting rid of space

    user_feeling = feeling.lower().strip()

    # Breaking the loop after "bye"

    if user_feeling == "bye":
        print("Byeeee!It was nice to chat with you! (o*￣▽￣*ブ)")
        break

    # Answering back the user according to the input

    elif user_feeling in positive:
        print(random.choice(positive_replies))

    elif user_feeling in neutral:
        print(random.choice(neutral_replies))

    elif user_feeling in negative:
        print(random.choice(negative_replies))

    else:
        print(random.choice(fallback_replies))