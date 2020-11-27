# Task 1

# class MyList(list):

#     def __getitem__(self, item):
#         a = self.index(item) + 1
#         return a

# x = MyList([1,2,3,4,5])
# print(x[1])


# Task 2

# class Student(dict):
    
#     def __init__(self, name, last_name, marks, grade):
#         self.name = name
#         self.last_name = last_name
#         self.grade = grade
#         self.marks = marks

#     def total_score(self, value):
#         score = 0
#         for v in value.values():
#             score += v
#             self.score = score

#     def __gt__(self, other):
#         if self.score > other.score:
#             print(f"{self.name}'s average score is equal to {self.score}. But {other.name}'s average score is less - {other.score}.")
#         else:
#             print(f"{self.name}'s average score is equal to {self.score}. But {other.name}'s average score is higher - {other.score}.")


#     def __lt__(self, other):
#         if self.score < other.score:
#             print(f"{self.name}'s average score is equal to {self.score}. But {other.name}'s average score is higher - {other.score}.")
#         else:
#             print(f"{self.name}'s average score is equal to {self.score}. But {other.name}'s average score is less - {other.score}.")


# bakyt = Student('Bakyt', 'Asanov', {'history': 89, 'math': 100, 'literature': 88}, 10)
# bakyt.total_score(bakyt.marks)
# begaiym = Student('Begaiym', 'Akmatova', {'history': 90, 'math': 85, 'literature': 90}, 10)
# begaiym.total_score(begaiym.marks)
# bakyt < begaiym
# begaiym < bakyt


