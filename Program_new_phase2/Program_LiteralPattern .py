#Literal Pattern
#service=0 / wild card pattern  ,   None / Literal Pattern
'''match service:
    case 1:
        print("ฝากเงิน")
    case 2:
        print("ถอนเงิน")    
    case 3:
        print("สอบถามยอดคงเหลือ")
    case _:#default case / wild card pattern
        print("ข้อมูลไม่ถูกต้อง")
'''
#capture pattern
'''service=1
match service:
    case 1:
        print("ฝากเงิน")
    case 2:
        print("ถอนเงิน")    
    case 3:
        print("สอบถามยอดคงเหลือ")
    case service:
        print(f"ไม่มีบริการหมายเลข {service} ในระบบ กรุณาทำรายการใหม่อีกครั้ง")'
'''
#Guard filter
# 100 = สอบได้คะแนนเต็ม , 50-99 = ผ่านเกณฑ์การสอบวัดผล
'''score=int(input("ป้อนคะแนนสอบของคุณ:"))
print("คะแนนสอบของคุณคือ:", score)
match score:
    case 100:
        print("ได้คะแนนเต็ม")
    case score if score >= 50 and score <=99:
        print("เกือบตก ไปลองมาใหม่นะ")
    case _:
        print("สอบไม่ผ่าน")
'''

#Or pattern
'''data=input("ป้อนเพศของคุณ:")
match data:
    case "เด็กชาย" | "นาย":
        print("เป็นเพศชาย")
    case "เด็กหญิง" | "นางสาว" | "นาง":
        print("เป็นเพศหญิง")
    case _:
        print("เป็นกะเทย")
'''

#Sequence pattern
'''data=[1,2,3]
match data:
    case[]:
        print("ไม่มีข้อมูล")
    case[1,2]:
        print("มีข้อมูล 2รายการ คือ 1และ2")
    case[1,2,3]:
        print("มีข้อมูล 3รายการ คือ 1 2และ3")
'''

#Mapping pattern
'''customers=[
    {"name" : "tang" , "type" : "member"},
    {"name" : "ta" , "type" : "general"},
    {"name" : "tan" , "type" : "general"}
]
id=int(input("ป้อนรหัสลูกค้า:"))
print(f"สวัสดีลูกค้ารหัส {id} : {customers[id],["name"]}")

match customers[id]:
    case { "type" : "member"}:
        print("คุณเป็นสมาชิกได้รับส่วนลด 50%")
    case _:
        print("ไม่ได้เป็นสมาชิก, ไม่ได้รับส่วนลด")
'''
























