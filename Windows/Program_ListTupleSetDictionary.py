#List
'''
product=["กางเกง",99.99,10,True] #วิธีที่1
product=list(("กางเกง",99.99,10,True)) #วิธีที่2

#เข้าถึงสมาชิก

print(product[0])
print(product[1])
print(product[2])
print(product[3])

product[0]="เสื้อ" #เปลี่ยนข้อมูลใน index
for element in product:
    print(element)

colors1=["ดำ","แดง","เขียว","ดำ",]
colors2=list(("ขาว","ฟ้า","ส้ม"))
fullcolors = colors1 + colors2 #รวมข้อมูลใน list
print(fullcolors)

colors=["แดง","เขียว","น้ำเงิน","ดำ","ขาว"]
print(colors[2:])
'''

#ฟังก์ชันจัดการ list
'''colors=["แดง","เขียว","น้ำเงิน","ดำ","ขาว"]
colors.append("น้ำตาล") #เพิ่มข้อมูลต่อท้าย 1 รายการ
colors.extend(["ส้ม","เหลือง","แดง"]) #เพิ่มข้อมูลต่อท้ายหลายรายการ
colors.insert(1,"เทา") #แทรกข้อมูล index ที่...
colors.remove("น้ำเงิน") #ลบเฉพาะค่า
colors.clear() #ลบทุกตัว
print(colors.count("แดง")) #นับ index ที่ซ้ำ

colors.sort()
colors.reverse()
print(colors)


#Tuple
product=("กางเกง",150.0,10)
(name,price,stock) = product
print(name)
print(price)
print(stock)
for item in product:
    print(item)

colors=("แดง","เขียว","น้ำเงิน","ดำ","ขาว")
print(colors.index("ดำ"))'''

#set
animals={"หมา","แมว","สิงโต","เสือ","ช้าง"}
animals.add("เป็ด")
animals.update(("หมู","ยีราฟ"))

pets=set(("หมา","แมว","กระต่าย","เม่น"))
print(animals)
print(pets)

data=animals.difference(pets)
print(data)