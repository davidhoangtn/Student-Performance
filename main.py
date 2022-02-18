import json
import os
from functions import avg_student_mark, hardest_subject, easiest_subject, best_performing_grade, worst_performing_grade, best_student_id, worst_student_id


NUM_STUDENTS = 1000
SUBJECTS = ["math", "science", "history", "english", "geography"]
GRADE = [1, 2, 3, 4, 5, 6, 7, 8]

def main():
    AVG_STUDENT_MARK = avg_student_mark(NUM_STUDENTS)
    HARDEST_SUBJECT = hardest_subject(NUM_STUDENTS, SUBJECTS)
    EASIEST_SUBJECT = easiest_subject(NUM_STUDENTS, SUBJECTS)
    BEST_PERFORMING_GRADE = best_performing_grade(NUM_STUDENTS, GRADE)
    WORST_PERFORMING_GRADE = worst_performing_grade(NUM_STUDENTS, GRADE)
    BEST_STUDENT_ID = best_student_id(NUM_STUDENTS)
    WORST_STUDENT_ID = worst_student_id(NUM_STUDENTS)
    print(f"Average Student Grade: {AVG_STUDENT_MARK}")
    print(f"Hardest Subject: {HARDEST_SUBJECT}")
    print(f"Easiest Subject: {EASIEST_SUBJECT}")
    print(f"Best Performing Grade: {BEST_PERFORMING_GRADE}")
    print(f"Worst Performing Grade: {WORST_PERFORMING_GRADE}")
    print(f"Best Student ID: {BEST_STUDENT_ID}")
    print(f"Worst Student ID: {WORST_STUDENT_ID}")

if __name__ == '__main__':
    main()
