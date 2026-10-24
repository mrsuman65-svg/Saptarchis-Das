score = 0

print("===== ULTIMATE QUIZ =====")

q = input("1. What is the capital of India? ").lower()
if q == "new delhi":
    score += 1
    print("Correct!")
elif q == "":
    print("No answer!")
else:
    print("Wrong!")

q = input("2. Which planet is called the Red Planet? ").lower()
if q == "mars":
    score += 1
    print("Correct!")
elif q == "":
    print("No answer!")
else:
    print("Wrong!")

q = input("3. How many players are in a football team? ")
if q == "11":
    score += 1
    print("Correct!")
elif q == "":
    print("No answer!")
else:
    print("Wrong!")

q = input("4. What is 12 × 8? ")
if q == "96":
    score += 1
    print("Correct!")
elif q == "":
    print("No answer!")
else:
    print("Wrong!")

q = input("5. Which is the largest planet? ").lower()
if q == "jupiter":
    score += 1
    print("Correct!")
elif q == "":
    print("No answer!")
else:
    print("Wrong!")

q = input("6. Who developed Python? ").lower()
if q == "guido van rossum":
    score += 1
    print("Correct!")
elif q == "":
    print("No answer!")
else:
    print("Wrong!")

q = input("7. How many days are in a leap year? ")
if q == "366":
    score += 1
    print("Correct!")
elif q == "":
    print("No answer!")
else:
    print("Wrong!")

q = input("8. Which animal is known as the King of the Jungle? ").lower()
if q == "lion":
    score += 1
    print("Correct!")
elif q == "":
    print("No answer!")
else:
    print("Wrong!")

q = input("9. What is the chemical symbol for water? ").lower()
if q == "h2o":
    score += 1
    print("Correct!")
elif q == "":
    print("No answer!")
else:
    print("Wrong!")

q = input("10. Which country won the 2022 FIFA World Cup? ").lower()
if q == "argentina":
    score += 1
    print("Correct!")
elif q == "":
    print("No answer!")
else:
    print("Wrong!")

print("\n===== RESULT =====")
print("Your score:", score, "/ 10")

if score == 10:
    print("🏆 PERFECT SCORE!")
elif score >= 7:
    print("🔥 Excellent!")
elif score >= 5:
    print("👍 Good job!")
else:
    print("📚 Keep practicing!")
