import numpy as np
#5 students × 3 subjects
#format:[Maths,English,Science]
scores = np.array([
    [85,55,92],  #student1
    [62,88,75],  #student2
    [95,48,86],  #student3
    [70,88,45],  #student4
    [88,75,70]   #student5
])


maths_scores =scores[:,0]
print(maths_scores)


english_scores = scores[:,1]
print(english_scores)

science_scores = scores[:,2]
print(science_scores)

average_student = np.mean(scores,axis=1)
print(average_student)

average_subject = np.mean(scores,axis=0)
print(average_subject)

passing_students =average_student >=60
print("passing students(True = pass, False=fail):",passing_students)

print("number of passing students:",np.sum(passing_students))

max_maths = np.max(maths_scores)
print(max_maths)

max_english = np.max(english_scores)
print(max_english)

max_science = np.max(science_scores)
print(max_science)
