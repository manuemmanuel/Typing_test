import time
import random

def generate_sentence():
    subjects = ["The dog", "The cat", "The rabbit", "The fox", "The bird"]
    verbs = ["jumps", "runs", "sleeps", "eats", "hops"]
    objects = ["over the fence", "on the mat", "under the tree", "into the hole", "across the river"]
    sentence = f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}"
    return sentence.capitalize() + '.'

def calculate_typing_speed(sentence, typing_time):
    words_typed = len(sentence.split())
    typing_speed = (words_typed / typing_time) * 60
    return typing_speed

def calculate_accuracy(sentence, user_input):
    correct_characters = 0
    total_characters = len(sentence)
    for i in range(total_characters):
        if i >= len(user_input):
            break
        if sentence[i] == user_input[i]:
            correct_characters += 1
    accuracy = (correct_characters / total_characters) * 100
    return accuracy

def run_typing_test():
    sentence = generate_sentence()
    print("Type the following sentence as quickly and accurately as possible:")
    print(sentence)
    input("Press enter to begin...")

    start_time = time.time()
    user_input = input()
    end_time = time.time()

    typing_time = end_time - start_time
    typing_speed = calculate_typing_speed(sentence, typing_time)
    accuracy = calculate_accuracy(sentence, user_input)
    print(f"Time taken: {typing_time:.2f} seconds")
    print(f"Typing speed: {typing_speed:.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    run_typing_test()
