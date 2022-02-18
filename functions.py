import json
def avg_student_mark(num_students):
    total_avg_mark = 0
    for i in range(1000):
        with open(f'students/{i}.json', 'r') as f:
            student = json.load(f)
            avg_mark = (student['math'] + student['science'] + student['history'] + student['english'] + student['geography']) / 5
            total_avg_mark += avg_mark
            avg_student_mark = round(total_avg_mark / 1000, 2)
    return avg_student_mark

def hardest_subject(num_students, subjects):
    score_dict = {subject:[] for subject in subjects}
    for i in range(num_students):
        with open(f'students/{i}.json', 'r') as f:
            student = json.load(f)
            for keys in score_dict.keys():
                if student[keys]:
                    score_dict[keys].append(student[keys])
    avg_subject_mark = {key:round(sum(value)/len(value), 2) for key, value in score_dict.items()}
    hardest_subject = min(avg_subject_mark, key=avg_subject_mark.get)
    return hardest_subject

def easiest_subject(num_students, subjects):
    score_dict = {subject:[] for subject in subjects}
    for i in range(num_students):
        with open(f'students/{i}.json', 'r') as f:
            student = json.load(f)
            for keys in score_dict.keys():
                if student[keys]:
                    score_dict[keys].append(student[keys])
    avg_subject_mark = {key:round(sum(value)/len(value), 2) for key, value in score_dict.items()}
    easiest_subject = max(avg_subject_mark, key=avg_subject_mark.get)
    return easiest_subject

def best_performing_grade(num_students, grades):
    grade_dict = {grade:[] for grade in grades}
    for i in range(num_students):
        with open(f'students/{i}.json', 'r') as f:
            student = json.load(f)
            avg_mark = (student['math'] + student['science'] + student['history'] + student['english'] + student['geography']) / 5
            for key in grade_dict.keys():
                if student['grade'] == key:
                    grade_dict[key].append(avg_mark)
    avg_grade_mark = {key:round(sum(value)/len(value), 2) for key, value in grade_dict.items()}
    best_performing_grade = max(avg_grade_mark, key=avg_grade_mark.get)
    return best_performing_grade

def worst_performing_grade(num_students, grades):
    grade_dict = {grade:[] for grade in grades}
    for i in range(num_students):
        with open(f'students/{i}.json', 'r') as f:
            student = json.load(f)
            avg_mark = (student['math'] + student['science'] + student['history'] + student['english'] + student['geography']) / 5
            for key in grade_dict.keys():
                if student['grade'] == key:
                    grade_dict[key].append(avg_mark)
    avg_grade_mark = {key:round(sum(value)/len(value), 2) for key, value in grade_dict.items()}
    worst_performing_grade = min(avg_grade_mark, key=avg_grade_mark.get)
    return worst_performing_grade

def best_student_id(num_students):
    i = 0
    highest_avg = 0
    best_student_id = None
    while i < num_students:
        with open(f'students/{i}.json', 'r') as f:
            student = json.load(f)
            avg_mark = (student['math'] + student['science'] + student['history'] + student['english'] + student['geography']) / 5
            
            if avg_mark > highest_avg:
                highest_avg = avg_mark
                best_student_id = student['id']
            i += 1
    return best_student_id

def worst_student_id(num_students):
    i = 0
    lowest_avg = 100
    worst_student_id = None
    while i < num_students:
        with open(f'students/{i}.json', 'r') as f:
            student = json.load(f)
            avg_mark = (student['math'] + student['science'] + student['history'] + student['english'] + student['geography']) / 5
            
            if avg_mark < lowest_avg:
                lowest_avg = avg_mark
                worst_student_id = student['id']
            i += 1
    return worst_student_id