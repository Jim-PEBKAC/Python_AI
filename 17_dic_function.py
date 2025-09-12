dic ={
    'name': 'lee,jimin',
    'phone': '010-1555-1212',
    'friends': ['Alice', 'Tom','John']
}

# dic.keys(): 특정한 사전의 키들만 가져와 dict_keys라는 객체를 반환
print(dic.keys())

for item in dic.keys():
    print(item)

# dict_keys → list 변환
keys=list(dic.keys())
print(keys)
print('키 리스트 변환')

#dic.values(): 특정 사전의 값만 가져와 dict_values 라는 객체를 반환
print(dic.values())

#list로 변환 시켜보자
val=list(dic.values())
print(val)
print('값 리스트 변환')

# dic.items(): 사전의 키:값을 한 쌍으로 가져와 dic_items로 반환: 가져온 한 쌍은 ()모양으로 튜플이다.
print(dic.items())
item=list(dic.items())
#list로 변환 시켜보자
print(item) # 리스트 안에 튜플로 존재하는 걸 확인 가능
print('아이템 리스트 변환')


# 값을 가져오기
print(dic['phone'])

#dic 안에 있는 모든 키와 값을 키:값 형태로 출력해 보자.
# print(f'name:{dic['name']},phone:{dic['phone']},friend:{dic['friends']}')
# print(f'{keys[0]}: {val[0]}, {keys[1]}: {val[1]}, {keys[2]}: {val[2]}')

for keys in dic.keys():
    print(f'{keys}: {dic[keys]}')

for item in dic.items():
    print(f'{item[0]}={item[1]}') # 튜플 형태로 나옴
print('------------------------------')

members = {
    'kim':63, 'lee':88, 'park':97, "gang":77, "hwang":100, "ga":65,
    "na":92, "la":90, "wang":100, "gu":79
}

# 90이상인 사람의 이름만 출력
print(members.keys())
key=list(members.keys())
print(key)

for key in members.keys(): # members_keys라는 객체를 반환한 것 안에서 key라는 리스트의 객체들을 반복해라
    if members[key] >= 90:
        print(f'{key}: {members[key]}')

print('------------------------------')

item=list(members.items())
print(item)

for item in members.items():
    if item[1] >= 90:
        print(f'{item[0]}: {item[1]}')

# key in dic: 해당 키가 사전에 존재하는지 확인
# 검색 시작 여부를 결정할 수 있는 방법 (내 예상으로는 추후 데이터 크롤링할 때 필요할듯..?
yn='kim' in members
print(f'kim이 있는가? {yn}')

yn='jung' in members
print(f'jung이 있는가? {yn}')
print('------------------------------')
# update: 이미 있는 키면 수정, 없는 키면 추가하는 함수
dic.update({'name':'홍길동','age':18,'marrid':False})
print(dic)

# dic.clear(): 사전안의 내용을 모두 지운다.
dic.clear()
print(dic)