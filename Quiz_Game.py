questions = [
    "What is the capital of France?",
    "Who painted the Mona Lisa?",
    "What is the largest planet in our solar system?",
    "What year did World War II end?",
    "Who wrote 'Romeo and Juliet'?",
    "What is the tallest mammal?",
    "What is the powerhouse of the cell?",
    "Who discovered penicillin?",
    "Which country is known as the Land of the Rising Sun?",
    "What is the chemical symbol for water?"
]
answers = [
    "Paris",
    "Leonardo da vinci",
    "Jupiter",
    "1945",
    "William shakespeare",
    "Giraffe",
    "Mitochondria",
    "Alexander fleming",
    "Japan",
    "H2O"
]
# Above questions and their answers are AI generated...

correct_answers = 0
wrong_answers = 0
user_answer = 0

print("...WellCome...To...My...Quiz...Game...")

for i in range(len(questions)):
    print(f"Youre {i + 1} question is:\t{questions[i]}")
    print(f"Options are:\na> {answers[0]}\t\tb> {answers[1]}\t\tc> {answers[2]}\nd> {answers[3]}\t\t\te> {answers[4]}"f"\t\tf> {answers[5]}\ng> {answers[6]}\t\th> {answers[7]}\t\ti> {answers[8]}\nj> {answers[9]}")
    user_answer = input().capitalize()
    if user_answer == answers[i]:
        print("Correct answer!")
        correct_answers += 1
    else:
        print("Wrong answer!")
        wrong_answers += 1

print("...Thanks for playing...")
print("You answered", correct_answers, "Correctly.")
print("You answered", wrong_answers, "Wrong")
