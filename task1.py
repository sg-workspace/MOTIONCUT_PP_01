import time

# Quiz Game Implementation

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        input("\nPress Enter to start the quiz...")
        for idx, question in enumerate(self.questions):
            print("\n" + question.prompt)
            user_answer = input("Enter your answer: ")
            if user_answer.lower() == question.answer.lower():
                print("\nCorrect!\n")
                self.score += 1
            else:
                print("\nIncorrect!\n")
            if idx != len(self.questions) - 1:  # Check if it's not the last question
                self.delay_and_countdown()
        
        print("Calculating your score...")
        time.sleep(2)  # Simulating calculation time
        print(f"\nYou scored {self.score}/{len(self.questions)}\n")

    def delay_and_countdown(self):
        time.sleep(1)  # Delay before showing the next question
        for i in range(3, 0, -1):  # Countdown before next question
            print(f"Next question in {i}...")
            time.sleep(1)


def main():
    # Define quiz questions
    question_prompts = [
        "What is the capital of France?\n(a) Paris\n(b) Rome\n(c) Berlin\n",
        "Which planet is known as the Red Planet?\n(a) Venus\n(b) Mars\n(c) Jupiter\n",
        "What is the powerhouse of the cell?\n(a) Nucleus\n(b) Ribosome\n(c) Mitochondria\n"
    ]
    questions = [
        Question(question_prompts[0], "a"),
        Question(question_prompts[1], "b"),
        Question(question_prompts[2], "c")
    ]

    # Create and run the quiz
    quiz = Quiz(questions)
    quiz.run_quiz()


if __name__ == "__main__":
    main()
