# Talon Bluemel
# UWYO COSC 1010
# 10/10/24
# HW 01
# Lab Section: 12
# Sources: ChatGPT, helped with finding the average scores inside a for loop.
# Homework Question: N/A




students = [
 {"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
 {"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
 {"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
 {"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
 ]
st_ave = {}
#Question 1
for student in students:
    name = student["name"]
    scores = student["scores"].values()
    ave_score = sum(scores) / len(scores)
    st_ave[name] = ave_score
#Question 2
print(st_ave)
#Question 3
for name, avg_score in st_ave.items():
    if avg_score > 80:
        print(f'{name}s average score was greater than 80.')

