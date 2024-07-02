minseok = ["김민석", "28", "01083663459"]
name = minseok[0]
age = minseok[1]
phone = minseok[2]


print(minseok, type(minseok))
print(name, age, phone)

names = [['강수경','강헤나','김민석'], ['20', '21', '23'], ['0101','0102','0103']]
print(names[0][0:2])

numbers = [1,2,3,4,5]
result = numbers[2] + numbers[4]
print(result)

print(len(names[0]))

# 리스트에 요소 추가하기
last = [1,2,3]
last.append(30)
print(last)
last.remove(3)
print(last)
print(type(last))