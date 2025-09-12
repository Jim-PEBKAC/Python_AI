dic ={
    'name': 'lee,jimin',
    'phone': '010-1555-1212',
    'friends': ['Alice', 'Tom','John']
}

# dic.keys(): 특정한 사전의 키들만 가져와 dict_keys라는 객체를 반환: 값이 들어간 키만 표기한다.
print(dic.keys())

for item in dic.keys():
    print(item)

# dict_keys → list 변환
keys=list(dic.keys())
print(keys)

#dic.values(): 특정 사전의 값만 가져와 dict_values 라는 객체를 반환: 키에 속한 값들만 표기한다.
print(dic.values())

#list로 변환 시켜보자
val=list(dic.values())
print(val)

# dic.items(): 사전의 키:값을 한 쌍으로 가져와 dic_items로 반환: 가져온 한 쌍은 ()모양으로 튜플이다.
print(dic.items())
item=list(dic.items())
#list로 변환 시켜보자
print(item) # 리스트 안에 튜플로 존재하는 걸 확인 가능

# 값을 가져오기
print(dic['phone'])

#dic 안에 있는 모든 키와 값을 키:값 형태로 출력해 보자.
# print(f'name:{dic['name']},phone:{dic['phone']},friend:{dic['friends']}')
# print(f'{keys[0]}: {val[0]}, {keys[1]}: {val[1]}, {keys[2]}: {val[2]}')

for keys in dic.keys():
    print(f'{keys}: {dic[keys]}')

for item in dic.items():
    print(f'{item[0]}={item[1]}') # 튜플 형태로 나옴
