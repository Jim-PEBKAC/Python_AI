# 콜라, 생수, 오렌지주스, 식혜, 이온음료
item='사과주스'

if item == '콜라':
    print(item+'가 나왔습니다.')
elif item == '생수':
    print(item+'가 나왔습니다.')
elif item == '오렌지주스':
    print(item + '가 나왔습니다.')
elif item == '식혜':
    print(item+'가 나왔습니다.')
elif item == '이온음료':
    print(item+'가 나왔습니다.')
else:
    print('없는 음료 입니다.')


# 강사님 코딩내용 *f-string 사용한 점이 다름
if item == '콜라':
    print(f'{item}가 나왔습니다.')
elif item == '생수':
    print(f'{item}가 나왔습니다.')
elif item == '오렌지주스':
    print(f'{item}가 나왔습니다.')
elif item == '식혜':
    print(f'{item}가 나왔습니다.')
elif item == '이온음료':
    print(f'{item}가 나왔습니다.')
else:
    print(f'{item}는 없는 음료 입니다.')