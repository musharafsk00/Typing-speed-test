import time
import random

def generate_random_sentence():
    sentences = ["The quick brown fox jumps over the lazy dog.",
                 "Programming is fun and challenging.",
                 "Practice makes perfect.",
                 "Coding is a valuable skill in today's world."]
    return random.choice(sentences)

def typing_speed_test():
    sentence = generate_random_sentence()
    print("Type the following:")
    print(sentence)

    input("Press Enter when you are ready to start typing...")
    start_time = time.time()

    user_input = input("Type the sentence: ")

    end_time = time.time()
    elapsed_time = end_time - start_time

    words_per_minute = (len(sentence.split()) / elapsed_time) * 60
    accuracy = calculate_accuracy(sentence, user_input)

    print(f"\nYour typing speed: {words_per_minute:.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")

def calculate_accuracy(original, user_input):
    correct_characters = sum(c1 == c2 for c1, c2 in zip(original, user_input))
    total_characters = max(len(original), len(user_input))
    accuracy = (correct_characters / total_characters) * 100
    return accuracy

if _name_ == "_main_":
    typing_speed_test()