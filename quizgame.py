class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question["question"])
        for i, option in enumerate(question["options"], 1):
            print(f"{i}. {option}")
        user_answer = input("Enter your answer (1/2/3/4): ")
        return int(user_answer) - 1

    def play_game(self):
        print("Welcome to the Quiz Game!")
        for question in self.questions:
            print("\n")
            user_answer_index = self.display_question(question)
            correct_answer_index = question["answer"]
            if user_answer_index == correct_answer_index:
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")
                print(f"The correct answer is: {question['options'][correct_answer_index]}")

        print("\nQuiz Complete!")
        print(f"Your final score is: {self.score}/{len(self.questions)}")
        percentage = (self.score / len(self.questions)) * 100
        print(f"You scored {percentage:.2f}%")

# Sample quiz questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Rome"],
        "answer": 1
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "answer": 0
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Leo Tolstoy"],
        "answer": 0
    }
]

# Create a QuizGame instance and play the game
game = QuizGame(questions)
game.play_game()
