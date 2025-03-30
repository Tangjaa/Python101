# Function with default parameters
def saveEmployee(name,department,salary=30000):
    print(f"ชื่อพนักงาน {name} ,แผนก {department}")
    print(f"เงินเดือน {salary} บาท")
    print("===================================")

#เรียกใช้งาน
saveEmployee("คุณตัง","IT")
saveEmployee("คุณเตย","HR",40000)
saveEmployee("คุณตาล","Finance",50000)
saveEmployee("คุณตาล","Finance")
