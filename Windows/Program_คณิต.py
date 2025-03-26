#แม่สูตรคูณ
'''number = int(input("ป้อนตัวเลขแม่สูตรคูณ"))

for i in range(1,101):
    print(number,"x",i," = ",number*i)

#หาผลรวมตัวเลข 5จำนวน
total=0
for i in range(1,6):
    number = int(input("ลำดับที่ "+str(i)+" : "))
    total+=number
print("ผลรวม = ",total)'''

#หาผลรวมตัวเลขไม่จำกัดจำนวน
total=0
while True:
    number = int(input("ป้อนตัวเลข:"))
    if number<=0:
        break
    total+=number
print("ผลรวม = ",total)
