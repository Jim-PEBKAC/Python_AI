# 사전은 키:값 형태로 되어있다.
# 비슷한 자료 구조로는 자바스크립트의 오브젝트, 자바의 맵이 있다/
dic={'name':'lee,jimin',
     'phone': '010-2345-1234',
     'age': '28'
     }
print(dic['name'])

dic2 = {
    'name':'park,jimin',
    'phone': '010-2445-1124',
    'friends':['Alice','John', 'Tom']
}

print(dic2)

# 사전에 데이터 넣기 1
a={'first':'a'}
print(a)

# 사전에 데이터 넣기 2
a['second']='b'
print(a)

# 사전에서 특정 요소 삭제
del a['second']
print(a)

# 사전의 특정 요소를 꺼내보자(사용법은 List와 비슷)
print(dic2['name'],dic2['friends'])
# get 메서드를 활용할 수 있으나 본인 마음이다.
print(dic2.get('phone'))
# 특정 키가 없는 경우, None이 아닌 대체 내용으로 반환할 수 있음
print(dic2.get('Tom','해당 내용이 없음'))