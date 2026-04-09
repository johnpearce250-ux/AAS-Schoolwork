
def parse_scores(text):
    """Turns the input text into a list of integer scores."""
    scores = []
    for score_str in text.split(','):
        try:
            score = int(score_str.strip())
            scores.append(score)
        except ValueError:
            print(f"Warning: '{score_str}' is not a valid integer and will be skipped.")
    return scores

def calculate_average(scores):
    """Calculates the average of a list of scores."""
    if not scores:
        return 0
    return sum(scores) / len(scores)

def map_score_to_letter(score):
    """Maps a numeric score to a letter grade."""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def letter_grade(avg):
    """Determines the letter grade based on the average score."""
    return map_score_to_letter(avg)

def main():
    input_scores = input("Enter scores separated by commas: ")
    scores = parse_scores(input_scores)
    average = calculate_average(scores)
    grade = letter_grade(average)
    print(f"Average Score: {average:.2f}")
    print(f"Letter Grade: {grade}")

if __name__ == "__main__":
    main()
