"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   a. Encapsulation: Object orientation allows you to have all data, variables
        and methods relating to one thing in one place.
   b. Abstraction: Object orientation makes it so that you can use methods
        without needing to understand their full functionality.
   c. Polymorphism: With object orientation, you can apply the same method to a
        number of different subclasses. Even though they are different, they can
        be treated in the same way. An analogy would be many different kinds of
        headphones can work in the same phone because they have the same kind of
        jack. Subclasses can all be different, but they can do the same kind of
        things with the same methods.

2. What is a class?
        A class is a type of data collection that can store its own
        data and methods. It is structured and customizable. When you create a
        class, you define all of the general behaviors that that category of
        objects can have.

3. What is an instance attribute?
        An instance attribute is a piece of data that is unique to an instance,
        or individual occurance, of a class. For example, in a hypothetical
        class called Animal, there might be an instance of the Animal class
        that has the name "Fido". Not all animals are named "Fido", so this name
        is an instance attribute to that particular instance of the Animal class.

4. What is a method?
        A method is a function defined within a class.

5. What is an instance in object orientation?
        An instance is an individual occurance of a class. An instance has all
        the attributes and methods definined within the class. It can also have
        instance attributes defined once the instance is created.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
        A class attribute is a piece of data tied to and true for that class and
        all instances of that class. An instance attribute is an attribute that
        is tied to a specific instance of a class. For example, if the class was
        HackbrightStudent, and each student is an instances of the class. All
        students share the class attributes of identifying as female and being
        software engineers, but we all have unique instance attributes
        that relate to our age, name, hometown, etc.

"""


# Parts 2 through 5:
# Create your classes and class methods


class Student(object):
    """A class of students and their information."""

    def __init__(self, first_name, last_name, address):
        """Create the basic information needed for an instance of Student."""
       
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """A class of questions and correct_answers."""

    def __init__(self, question, correct_answer):
        """Create a question and correct_answer for an instance of Question."""
      
        self.question = question
        self.correct_answer = correct_answer


    def ask_and_evaluate(self):
        """Prints the question to console and prompts the user for an answer.
            Returns True if answer is the correct_answer, or False if not.
        """
        answer = raw_input(self.question + " > ")
        return answer == str(self.correct_answer)  # Account for non-string self.correct_answer 


class Exam(object):
    """A class of exams and questions."""

    def __init__(self, name):
        """Create a new exam class."""

        self.name = name
        self.questions = []


    def add_question(self, question, correct_answer):
        """Adds a question and correct_answer to the Exam's list of questions."""

        self.questions.append(Question(question, correct_answer))


    def administer(self):
        """Asks all questions and returns the score as a decimal percentage."""

        score = 0.0
        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1.0

        final_score = score / len(self.questions)
        return final_score


# Part 4:

def take_test(Exam, Student):
    """Administers the exam and assigns a score to the student."""

    score = Exam.administer()
    Student.score = score
    print "{} {}'s score is {:.2f}.".format(Student.first_name,
                                            Student.last_name,
                                            Student.score)


def example():
    """Creates an exam, adds questions to the exam, creates a student,
        administers the exam for that student.
    """
    exam = Exam('midterm')
    exam.add_question('What color is the sky on a sunny day?', 'blue')
    exam.add_question('What color is healthy grass?', 'green')
    exam.add_question('Who is the author of Python?', 'Guido Van Rossum')
    student = Student('Example', 'Student', '123 Main Street')
    take_test(exam, student)

    # ALTERNATE SOLUTION INCASE USER WAS SUPPOSED TO CREATE EXAM & STUDENT:

    # exam = Exam(raw_input("What is your example exam called? > "))
    # exam.add_question('What color is the sky on a sunny day?', 'blue')
    # exam.add_question('What color is healthy grass?', 'green')
    # exam.add_question('Who is the author of Python?','Guido Van Rossum')
    # student = Student(raw_input("What is your example student's first name? > "),
    #                   raw_input("What is your example student's last name? > "),
    #                   raw_input("What is your example student's address? > "))
    # take_test(exam, student)


# Part 5:

class Quiz(Exam):
    """A subclass of exam that assesses quizzes as pass/fail."""

    def administer(self):
        """Administers the Quiz and returns True if passed or False if failed."""

        percentage_score = super(Quiz, self).administer()
        return percentage_score >= 0.5
