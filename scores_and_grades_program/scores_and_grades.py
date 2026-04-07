scores_dict={}
while True:
    name=input("Student's name: ")
    if name == "done":
        break
    try:
    grade = int(input("Student's grade: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer grade.")
        continue
    scores_dict[name] = grade

def letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"
    
for name, score in sorted(scores_dict.items()):
    print(f"{name}: {score}: {letter(score)}")