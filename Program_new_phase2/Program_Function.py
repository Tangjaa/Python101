#สร้าง Function
def sayHello(time,username,age):#parameter
    print("สวัสดีครับ",username) 
    print("ปีนี้คุณมีอายุ",age,"ปี")

def saveEmployee(name,department,salary):
    print(f"ชื่อ {name} ,แผนก {department}")
    print(f"เงินเดือน {salary} บาท")
    print("===================================")

def showTable(num):
    print(f"-----------แม่ {num}------------")
    for i in range(1,13):
        print(f"{num} x {i} = {2*i}")

#เรียกใช้งาน
#myTime = "ตอนเช้า" 
#sayHello(myTime,"คุณตัง",27) #argument
#sayHello(myTime,"คุณเตย",72)
#showTable(3)
#showTable(5)
#showTable(12)

saveEmployee("คุณตัง","IT",30000)
saveEmployee("คุณเตย","HR",40000)
saveEmployee("คุณตาล","Finance",50000)