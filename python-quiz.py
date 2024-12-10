import time

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            time.sleep(1)
            print("\n""You got it right pal!\n")
            score += 1
            time.sleep(2)
        else:
            time.sleep(1)
            print("\n""Sorry pal... that was wrong! The correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")
    time.sleep(2)


# List of quiz questions. Each question is a dictionary.
questions = [
    {
        "prompt": "What is the largest country in the world by land area?",
        "options": ["A. Russia", "B. Canada", "C. China", "D. United States"],
        "answer": "A"
    },
    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "B"
    },
    {
        "prompt": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "prompt": "Which country is famous for the Taj Mahal?",
        "options": ["A. China", "B. Egypt", "C.  India", "D.  Italy"],
        "answer": "C"
    }
]

# Run the quiz
run_quiz(questions)