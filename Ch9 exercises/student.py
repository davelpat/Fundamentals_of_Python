"""
Instructions for programming Exercise 9.1

Add three methods to the Student class that compare twoStudent objects. One
method (__eq__) should test for equality. A second method (__lt__) should test
for less than. The third method (__ge__) should test for greater than or equal
to. In each case, the method returns the result of the comparison of the two
students’ names. Include a main function that tests all of the comparison
operators.

"""

"""
File: student.py
Resources to manage a student's name and test scores.
"""

from random import shuffle


class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]

    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __lt__(self, other):
        """Compares two students' names.
        Returns True if the first name comes first alphabetically."""
        return self.name < other.getName()

    def __eq__(self, other):
        """Compares two students' names.
        Returns True if the names are the same."""
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.name == other.getName()

    def __ge__(self, other):
        """Compares two students' names.
        Returns True if the names are the same."""
        return self.name >= other.getName()


    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name + "\nScores: " + \
               " ".join(map(str, self.scores))


def main():
    """A simple test."""
    num_scores = 5
    ken = Student("Ken", num_scores)
    ken2 = ken
    lisa = Student("Lisa", num_scores)
    kenneth = Student("Ken", num_scores)
    bill = Student("Bill", num_scores)
    tony = Student("Tony", num_scores)
    students = [ken, lisa, bill, tony]
    base_score = 75
    for student in students:
        for i in range(1, 6):
            student.setScore(i, base_score)
            base_score += 1
        # print(student)

    print("Comparison tests:\n")

    print("ken < lisa:", str(ken < lisa))
    print("lisa < kenneth:", str(lisa < kenneth))

    print("ken == kenneth:", str(ken == kenneth))
    print("ken == ken2:", str(ken == ken2))
    # print("2 == ken2:", str(2 == ken2))  # causes an error
    print("lisa == kenneth:", str(lisa == kenneth))

    print("lisa >= kenneth:", str(lisa >= kenneth))
    print("ken >= kenneth:", str(ken >= kenneth))
    print("ken >= lisa:", str(ken >= lisa))

    print("lisa <= kenneth:", str(lisa >= kenneth))
    print("ken <= kenneth:", str(ken >= kenneth))
    print("ken <= lisa:", str(ken >= lisa))

    print("ken > lisa:", str(ken < lisa))
    print("lisa > kenneth:", str(lisa < kenneth))

    print("\nSorted list of students:")
    # Create the required list of Students
    num_scores = 10
    lyst = []
    for i in range(1, 6):
        lyst.append(Student("Name"+str(i), num_scores))
    # Disorder & reorder the list, then print it
    shuffle(lyst)
    lyst.sort()
    for student in lyst:
        print(student)


if __name__ == "__main__":
    main()
