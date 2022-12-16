import speech_recognition as sr
import random

# print(sr.__version__)

# Creating recognizer instance
r = sr.Recognizer()
score = 0
list_of_words = []


# Function listen to words from microphone and return capitalize string of the word
def voice_detected_words(r):
    # using mic
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            words = r.recognize_google(audio, show_all=False, with_confidence=False)
        except sr.UnknownValueError:
            return print("Google dont know what you are talking about")
        return words.capitalize()


# Add all words in words text file to list
with open('words.txt') as file:
    for line in file:
        if '\n' not in line:
            list_of_words.append(line)
        else:
            list_of_words.append(line[:-1])

print("Welcome to Pronounce the word!")
num_of_words = int(input("Select how many words would you like to try pronouncing: "))
# Shuffle the list and print number of words specified by user
random.shuffle(list_of_words)
print(list_of_words[:num_of_words])
# Process the word and check if word detected from mic is same as word shown
turn = 1
wrong_words = []
while turn < num_of_words + 1:
    print(f"Turn {turn}: {list_of_words[turn - 1]}")
    if voice_detected_words(r) == list_of_words[turn - 1]:
        print("Correct!")
        score += 1
    else:
        wrong_words.append(list_of_words[turn-1])
    turn += 1

print(f"Your total score is {score}, you got the word/s {wrong_words} wrong")
