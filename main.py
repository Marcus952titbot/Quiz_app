import random 

#list of quiz questions

quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": 1
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": 2
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "answer": 2
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["Harper Lee", "J.K. Rowling", "Mark Twain", "Ernest Hemingway"],
        "answer": 1
    }
]

def run_quiz():
    questions = quiz_questions[:]
    random.shuffle(questions)
    score = 0


    for q in questions:
        print(q['question'])
        for idx, option in enumerate(q['options'], start=1):
            print(f"{idx}. {option}")
        max_choice = len(q['options'])
        while True:
            raw = input(f"Your answer (1-{max_choice}): ").strip()
            if not raw.isdigit():
                print("Invalid input. Please enter a number.")
                continue
            choice = int(raw)
            if 1 <= choice <= max_choice:
                break
            print(f"Please enter a number between 1 and {max_choice}.")
        if choice == q['answer']:
            print("Correct!")
            score += 1
        else:
            correct_text = q['options'][q['answer'] - 1]
            print(f"Wrong! The correct answer is: {correct_text}")
    print("\n---Quiz complete---")
    print(f"Your final score is: {score}/{len(quiz_questions)}")
    print("Thank you for playing!")

if __name__ == "__main__":
 run_quiz()