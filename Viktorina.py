# -*- coding: utf-8 -*-

class HistoryQuiz:
    def __init__(self):
        self.score = 0
        self.correct_answers = []
        self.incorrect_answers = []

    def run_quiz(self):
        print("Добро пожаловать в викторину по истории Кыргызстана!")
        print("Ответьте на 10 вопросов.")

        for i in range(1, 11):
            question_obj = HistoryQuestion(i)
            question_obj.display_question()

            user_answer = input("Выберите вариант ответа (a, b, c): ").lower()

            if question_obj.check_answer(user_answer):
                print(f"Верно! +1 балл\n")
                self.score += 1
                self.correct_answers.append(f"Вопрос {i}: Ваш ответ - {user_answer.upper()}")
            else:
                correct_option = question_obj.get_correct_option().upper()
                print(f"Неверно. Правильный ответ: {correct_option}\n")
                self.incorrect_answers.append(f"Вопрос {i}: Ваш ответ - {user_answer.upper()}, Правильный ответ - {correct_option}")

        self.display_results()

    def display_results(self):
        print("Викторина завершена! Ваши результаты:")
        print(f"Итоговый счет: {self.score} из 10.\n")

        self.display_answers("Правильные ответы", self.correct_answers)
        self.display_answers("Неправильные ответы", self.incorrect_answers)

    def display_answers(self, title, answers):
        if answers:
            print(f"{title}:")
            for answer in answers:
                print(answer)

class HistoryQuestion:
    def __init__(self, question_number):
        self.question_number = question_number
        self.question, self.options, self.correct_option = self.get_history_question()

    def get_history_question(self):
        questions = {
            1: ("1. Когда был провозглашен суверенитет Кыргызстана?", ["a. 1991", "b. 1995", "c. 2000"], "a"),
            2: ("2. Кто был первым президентом Кыргызстана?", ["a. Алмазбек Атамбаев", "b. Роза Отунбаева", "c. Аскар Акаев"], "c"),
            3: ("3. Какая гора является самой высокой в Кыргызстане?", ["a. Пик Ленина", "b. Пик Победы", "c. Пик Коммунизма"], "b"),
            4: ("4. В каком году Кыргызстан стал членом ООН?", ["a. 1991", "b. 1992", "c. 1993"], "c"),
            5: ("5. Какое крупное озеро находится в северной части Кыргызстана?", ["a. Сары-Кел", "b. Иссык-Куль", "c. Сары-Челек"], "b"),
            6: ("6. Какая река является самой длинной в Кыргызстане?", ["a. Чу", "b. Талас", "c. Нарын"], "a"),
            7: ("7. В каком году произошла тюркская великая миграция в Кыргызстан?", ["a. IX век", "b. XI век", "c. XIII век"], "b"),
            8: ("8. Какой город является столицей Кыргызстана?", ["a. Бишкек", "b. Ош", "c. Джалал-Абад"], "a"),
            9: ("9. Кто был основателем Киргизской ССР?", ["a. Алымбек Даана", "b. Молдо Суев", "c. Михаил Фрунзе"], "c"),
            10: ("10. Какой культурный объект в Кыргызстане включен в список Всемирного наследия ЮНЕСКО?", ["a. Суулукташ", "b. Береке", "c. Суурикен"], "a"),
        }

        return questions.get(self.question_number, ("Вопрос не определен.", [], ""))

    def display_question(self):
        print(self.question)
        for option in self.options:
            print(option)

    def check_answer(self, user_answer):
        return user_answer == self.correct_option

    def get_correct_option(self):
        return self.correct_option


if __name__ == "__main__":
    history_quiz = HistoryQuiz()
    history_quiz.run_quiz()