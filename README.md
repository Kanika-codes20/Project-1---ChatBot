# Project-1---ChatBot
# ChatBOT BananaMilkshake 

A beginner-friendly Python chatbot created while learning the fundamentals of Python programming.

The chatbot interacts with the user, asks for their name and how they are feeling, and responds based on different categories of input.

## Features

* Greets the user when the program starts.
* Asks for the user's name.
* Responds to the user's mood.
* Recognizes positive, neutral, and negative responses.
* Uses random responses to make conversations less repetitive.
* Continues the conversation using a `while` loop.
* Allows the user to end the conversation by typing `bye`.
* Provides a fallback response when it does not recognize the input.

## Python Concepts Used

* `input()`
* Variables
* Strings
* String concatenation
* Lists
* `if`, `elif`, and `else`
* `while` loops
* `break`
* `import`
* `random.choice()`
* `.lower()`
* `.strip()`
* The `in` operator
* Comments

## How It Works

The chatbot first asks the user for their name and greets them.

It then repeatedly asks how the user is doing. The response is cleaned using `.lower()` and `.strip()` so that differences in capitalization and extra spaces do not affect the matching.

The chatbot checks whether the response belongs to one of three categories:

* Positive
* Neutral
* Negative

It then randomly selects a response from the corresponding response list.

If the chatbot does not recognize the input, it chooses a response from a fallback list.

The conversation continues until the user enters `bye`.

## How to Run

1. Make sure Python is installed on your computer.
2. Download or clone this repository.
3. Open the project in Python IDLE, PyCharm, or another Python editor.
4. Run `chatbot.py`.
5. Follow the instructions displayed in the terminal.

## Example

```text
Welcome to the ChatBOT BananaMilkshake❤
What is your name? Alex
Nice to meet you, Alex!
That's a lovely name!

How are you doing? great
Niceeee, keep going...!

How are you doing? bye
Byeeee! It was nice to chat with you! (o*￣▽￣*ブ)
```

## What I Learned

This was one of my beginner Python projects. While building it, I practiced taking user input, working with lists, using conditional statements and loops, importing modules, cleaning user input, and selecting random responses.

The project helped me understand how multiple basic Python concepts can be combined to create an interactive program.

## Limitations

This is a rule-based beginner chatbot. It does not use artificial intelligence or natural language processing, so it can only respond to inputs that match the responses programmed into it.

## Future Ideas

Possible future improvements could include:

* More conversation topics
* More recognized responses
* Additional chatbot commands
* A larger response database

---

Made as a beginner Python learning project. :)

