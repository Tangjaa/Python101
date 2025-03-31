#Arguments 
#args / kwargs
#ข้อมูลแบบลำดับ *args (tuple)
#ข้อมูลแบบไม่ลำดับ หรือ กำหนดชื่อ **kwargs (dictionary)

def saveEmployee(**kwargs): #dictionary
    print(f"ชื่อพนักงาน {kwargs["name"]} ,แผนก {kwargs["department"]}")
    print(f"เงินเดือน {kwargs["salary"]} บาท")
    print(f"ที่อยู่ {kwargs["country"]}")
    print("===================================")

#เรียกใช้งาน
saveEmployee(name="ตัง",department="IT",salary=30000,country="กรุงเทพ")
saveEmployee(name="เตย",department="HR",salary=40000,country="นนทบุรี")
saveEmployee(name="ตาล",department="Finance",salary=50000,country="ปทุมธานี")
