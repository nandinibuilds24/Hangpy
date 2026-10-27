from words import questions


class HangmanGame:

    def __init__(self):
        self.current_index = 0
        self.score = 0
        self.wrong_attempts = 0
        self.max_attempts = 6

    def get_question(self):
        """
        Returns the current question.
        Questions are given sequentially.
        """

        if self.current_index >= len(questions):
            return None

        return questions[self.current_index]

    def check_answer(self, user_answer):
        """
        Checks whether the user's answer is correct.
        """

        current_question = self.get_question()

        if user_answer.strip().lower() == current_question["answer"].lower():

            self.score += 10
            return True

        self.wrong_attempts += 1
        return False

    def get_hint(self):
        """
        Returns the hint for the current question.
        """

        current_question = self.get_question()

        return current_question["hint"]

    def chances_left(self):
        """
        Returns the number of remaining chances.
        """

        return self.max_attempts - self.wrong_attempts

    def is_game_over(self):
        """
        Checks whether the player has used all 6 chances.
        """

        return self.wrong_attempts >= self.max_attempts

    def next_question(self):
        """
        Moves to the next question.
        """

        self.current_index += 1
        self.wrong_attempts = 0

    def is_finished(self):
        """
        Checks whether all questions are completed.
        """

        return self.current_index >= len(questions)