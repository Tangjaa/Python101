#break / continue
'''for counter in range(1,11):
    if counter==5:
        break  #หยุดรอบที่กำหนด
    print(counter)
print("จบการทำงาน")'''

for counter in range(1,11):
    if counter%2==0:
        continue   #กระโดดข้ามรอบ(เงื่อนไข)ที่กำหนด
    print(counter)
print("จบการทำงาน")