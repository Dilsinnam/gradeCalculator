print(
    "This is a score calculator for COP3502C. All values have been adjusted as of 1/16/2024 at 7:43 PM EST."
)
assignment = float(input("Please enter your assignment grade: "))
exam = float(input("Please enter your exam grade: "))
lab = float(input("Please enter your lab grade: "))
quiz = float(input("Please enter your quiz grade: "))
project = float(input("Please enter your project grade: "))
gProject = float(input("Please enter your group project grade: "))
zyBooks = float(input("Please enter your ZyBooks grade: "))
lecture = float(input("Please enter lecture grade: "))

totalScore = (
    assignment * 0.16
    + exam * 0.30
    + lab * 0.16
    + quiz * 0.16
    + gProject * 0.10
    + zyBooks * 0.2
    + lecture * 0.2
)
print("Your score for this semester is:", totalScore)
