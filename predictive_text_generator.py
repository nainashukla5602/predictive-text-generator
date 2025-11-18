

from collections import defaultdict
import random


training_text = """
I love to play football and I love to watch movies.
I have a passion for programming and I love Python.
Python is easy to learn and fun to use.

I enjoy reading books and exploring new places.
Machine learning helps computers make smart predictions.
Artificial intelligence is growing very fast.
Chatbots are becoming more popular every day.
Coding improves problem-solving skills.
"""

# Clean and split text
words = training_text.lower().split()


model = defaultdict(list)

for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    model[current_word].append(next_word)


# --------------------------------------
# STEP 3: PREDICTION FUNCTION
# --------------------------------------

def predict_next_word(input_word):
    input_word = input_word.lower()
    if input_word in model:
        return random.choice(model[input_word])
    else:
        return "No prediction available"


# --------------------------------------
# STEP 4: USER INTERACTION
# --------------------------------------

print("----- Predictive Text Generator -----")
print("Type a word and get the next-word prediction.")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("Enter a word: ")

    if user_input.lower() == "exit":
        print("Program ended.")
        break

    prediction = predict_next_word(user_input)
    print("Predicted next word:", prediction)