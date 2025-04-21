#Lambda finction 2^3
'''def power(base,n):
    return base**n
result = power(2,3)
print("ผลลัพธ์ = ", result()''' #แบบกำหนดชื่อ
result = lambda base,n : base**n #แบบไม่กำหนดชื่อ
print("ผลลัพธ์ = ", result(2,3)) 