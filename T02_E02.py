def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"


valid_scores = []

for token in input().split():
    if token.isascii() and token.isdigit():
        score = int(token)
        if score <= 100:
            valid_scores.append(score)
            print(f"{score}: {grade(score)}")
            continue
    print(f"{token}: invalid")

if valid_scores:
    average = sum(valid_scores) / len(valid_scores)
    print(f"Average of valid scores: {average:.1f}")
else:
    print("No valid scores")