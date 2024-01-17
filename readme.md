# Grade Calculator

A very simple grade calculator made with Python, as in intro to COP3502.

## Result

```python
assignment = float(input("Please enter your assignment grade: "))
exam = float(input("Please enter your exam grade: "))
lab = float(input("Please enter your lab grade: "))
etc, you get the idea

#Combining the scores
totalScore = assignment*0.16 + exam*0.30 + lab*0.16 + quiz*0.16 + gProject*0.10 + zyBooks*0.2 + lecture*0.2

#The final score
print("Your score for this semester is:", totalScore)
```
