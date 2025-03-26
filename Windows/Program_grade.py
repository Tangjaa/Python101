#โปรแกรมตัดเกรด
#input
score = int(input("ป้อนคะแนนสอบของคุณ:"))
print("คะแนนของคุณ คือ ",score)
grade=None

#process
if score>=80 and score<=100:
    grade="A"
elif score>=60 and score<=79:
    grade="B"
elif score>=0 and score<=59:
    grade="F"
else:
    grade="N (Invalid score)"

#output
print("เกรดของคุณ คือ ",grade)