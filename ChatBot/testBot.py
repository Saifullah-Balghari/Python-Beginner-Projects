import json
from difflib import get_close_matches as gcm


def load_memory(file_path: str) -> dict:
    """ Takes a file path as input, reads JSON data from the file,
    and returns it as a dictionary"""
    with open(file_path, "r") as f:
        data: dict = json.load(f)
    return data


def save_memory(file_path: str, data: dict):
    """ Takes in a file path and a dictionary, and saves the dictionary into a 
    file path(JSON file) with specified indentation"""
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)


def best_matches(user_ques, questions):
    """ Finds the best match with the accuracy of 60%"""
    matches = gcm(user_ques, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None


def get_ans_4_question(question: str, memory: dict):
    for i in memory["questions"]:
        if i["question"] == question:
            return i["answer"]


def main():
    memory = load_memory('memory.json')

    while True:

        user_input: str = input("You: ")

        if user_input.lower() == 'quit':
            break

        best_match = best_matches(user_input, [ i ['question'] for i in memory['questions']])

        if best_match:
            answer: str = get_ans_4_question(best_match, memory)
            print(f"Bot: {answer}")
        
        else:
            print("Bot: I don\'t know the answer. Can you teach me? if yes please provide a correct answer and don\'t use extra words.")
            new_answer: str = input("Type the answer or 'skip' to skip: " )

            if new_answer.lower() != 'skip':
                memory["questions"].append({"question": user_input, "answer": new_answer})
                save_memory('memory.json', memory)
                print("Thanks for teaching me!")


if __name__ == "__main__":
    main()