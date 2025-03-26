#nested loop2
'''for i in range(2):
    print("รอบที่ ",i)
    for j in range(3):
        print(j)'''
#แม่สูตรคูณแบบกำหนดช่วง
start=int(input("แม่สูตรคูณเริ่มต้น :"))
end=int(input("แม่สูตรคูณเริ่มต้น :"))

for number in range(start,end+1):
    print("สูตรคูณแม่ ",number)
    print("............")
    for i in range(1,13):
        print(number,"x",i," = ",number*i)
    print("............")