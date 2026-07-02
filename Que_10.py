import numpy as np

marks = np.random.randint(30,101,(10,5))
print(marks)

total= marks.sum(axis = 1)
print("\n",total)

average = marks.mean(axis = 1)
print("\n",average)

lowest = total.argmin()
highest = total.argmax()
print("\n",highest)
print("\n",lowest)

print("\n","mean =",marks.mean())
print("\n","Standard deviation=",marks.std())

top3 = total.argsort()[-3:]

print("\nTop 3 Students Index:")
print(top3)

print("\nMarks of Top 3 Students:")
print(marks[top3])


# Comments:
# sum(axis=1) calculates total marks.
# mean(axis=1) calculates average marks.
# argmax() and argmin() find highest and lowest scorers.
# argsort() helps find top students.