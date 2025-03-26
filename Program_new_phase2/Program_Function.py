#สร้าง Function
def sayHello(username,age):#parameter
    print("สวัสดีครับ",username) 
    print("ปีนี้คุณมีอายุ",age,"ปี")

def showTable():
    print("-------")
    for i in range(1,13):
        print(f"2 x {i} = {2*i}")



#เรียกใช้งาน
sayHello("คุณตัง",27) #argument
sayHello("คุณเตย",72)


