'''
#ตัวดำเนินการทางคณิตศาสตร์
number1,number2=10,2

print("ตัวเลขที่ 1 =",number1)
print("ตัวเลขที่ 2 =",number2)

#คำนวน
print("===========")
print("ผลบวก =",number1+number2)
print("ผลลบ =",number1-number2)
print("ผลคูณ =",number1*number2)
print("ยกกำลัง =",number1**number2)
print("ผลหาร =",number1/number2)
print("ผลหารไม่เอาทศนิยม =",number1//number2)
print("เศษ =",number1%number2)

#ตัวดำเนินการกำหนดค่า (assignment operator)
x,y=10,2

print("x =",x)
print("y =",y)

x+=y #12
print("ผลลัพธ์บวก =",x)
x-=y
print("ผลลัพธ์ลบ =",x)
x*=y
print("ผลลัพธ์คูณ =",x)
x**=y
print("ผลลัพธ์ยกกำลัง =",x)
x/=y
print("ผลลัพธ์หาร =",x)
x//=y
print("ผลลัพธ์หารไม่เอาทศนิยม =",x)
x%=y
print("ผลลัพธ์เศษ =",x)

#ตัวดำเนินการเปรียบเทียบ (assignment operator)
x,y=100,50
print("x==y จริงไหม",x==y)
print(x==y)
print(x!=y)
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)
'''
#คำสั่งเงื่อนไข
#IF Statement -> if 1เงื่อนไข, if-else 2เงื่อนไข, if-elif-else หลายเงื่อนไข
'''
#input
score = int(input("กรุณาป้อนคะแนนสอบของคุณ:"))
print("คะแนนสอบของคุณ =",score)
print(type(score))

#process
if score<0:
    print("คะแนนไม่ถูกต้อง")
elif score>=50:
    print("สอบผ่าน")
else:
    print("สอบไม่ผ่าน")

#ternary operator
number = int(input("ป้อนตัวเลขของคุณ:"))
print("ตัวเลขของคุณ คือ",number)
print("เลขคู่")if number%2==0 else print("เลขคี่")
'''

#ตัวดำเนินการทางตรรกศาสตร์
username=input("ป้อนชื่อผู้ใช้:")
password=input("ป้อนรหัสผ่าน:")

if username=="admin" and password=="1234":
    print("เข้าสู่ระบบสำเร็จ")
else:
    print("ข้อมูลไม่ถูกต้อง")





















