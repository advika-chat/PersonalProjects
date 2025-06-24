from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def print(self):
        pass
    
    @abstractmethod
    def check(self, answer):
        pass

class YesNoQuestion(Question):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    
    def print(self):
        print(f"[?] {self.question} (yes/no)")
    
    def check(self, answer):
        return (answer.lower() == 'yes' and self.answer) or (answer.lower() == 'no' and not self.answer)

class OpenQuestion(Question):
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers
    
    def print(self):
        print(f"[?] {self.question}")
    
    def check(self, answer):
        return answer in self.answers

class MultiOptionsQuestion(Question):
    def __init__(self, question, options, answer_index):
        self.question = question
        self.options = options
        self.answer_index = answer_index

    def print(self):
        print(f"[?] {self.question}")
        for i, option in enumerate(self.options):
            print(f"[{i+1}] {option}")

    def check(self, answer):
        try:
            return int(answer) == self.answer_index + 1
        except ValueError:
            return False

class Quiz:
    def __init__(self, questions):
        self.questions = questions
    
    def start(self):
        results = []
        for question in self.questions:
            question.print()
            print()
            res = question.check(input('[+] '))
            results.append(res)
            print()
            print()
        self.print_results(results)

    def print_results(self, results):
        correct_answers = len([x for x in results if x])
        print("Your score is " + str(correct_answers) + '/' + str(len(results)))
        print()
        for i in range(len(results)):
            print('[' + str(i + 1) + '] ' + ('Pass' if results[i] else 'Fail'))

# Sample questions for testing
q1 = OpenQuestion("How to say 'Hello' in French?", ["Ni Hao", "Bonjour", "Namaste"])
q2 = YesNoQuestion("Bats are blind", False)
q3 = MultiOptionsQuestion("What does B stand for in VIBGYOR?", ["Red", "Blue", "Green"], 1)  # 1 is the index for "Blue"

# Create a quiz with these questions
quiz = Quiz([q1, q2, q3])

# Start the quiz
quiz.start()
