# warmup4
# hello test

def is_valid_score(score):
    return 0 <= score <= 100

score = int(input("Enter a score: "))

if is_valid_score(score):
    print("Valid Score")
else:
    print("Invalid Score; enter a integer from 0-100, inclusive. ")

