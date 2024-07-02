name = input('이름을 입력하세요:')
age = input('나이를 입력하세요:')
mail = input('이메일 주소를 입력하세요:')
phone = input('연락처를 입력하세요:')
dic = {name:{'이름':name}}
last = ["나이:",age, "이메일주소:",mail,"전화번호:",phone]
print(dic[name],last)

name2 = input('이름을 입력하세요:')
age2 = input('나이를 입력하세요:')
mail2 = input('이메일 주소를 입력하세요:')
phone2 = input('연락처를 입력하세요:')
dic2 = {name2:{'이름':name2}}
last2 = ["나이:",age2, "이메일주소:",mail2,"전화번호:",phone2]
print(dic2[name2],last2)