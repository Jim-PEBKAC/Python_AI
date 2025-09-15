name='lee ji-min'
content="My content"

# 여러줄의 문자열을 변수에 담을 때
multi = '''this is a multi line string
this is second line'''

print('name: '+name)
print('content: '+content)
print('multi: '+multi)

# 과거 사용 방식(참고만)
# 문자열에 다른 타입의 데이터를 함께 출력할 경우 (.format)
# str() 안에 숫자나 뭔가를 넣었을 때 글자로 인식시키는 함수
age = 33

print('내 이름은 {0}이고 나이는 {1} 입니다.'.format(name,age))
print('내 이름은 '+name+'이고 나이는 '+str(age)+'입니다.')

# 최신 방식
print(f'내 이름은 {name} 이고 나이는 {age} 입니다.')
print('내 이름은 {name} 이고 나이는 {age} 입니다.') # f-string 즉, f를 안 넣으면 변수를 인식 못함

# 여러 줄 -> 한 줄 / 한 줄 -> 여러 줄로 바꾸는 방법 (\n(출력할 때나 의미 있을 듯)와  \(별 의미 없을 듯))
print('이것은 한 줄이지만\n 여러 줄처럼 보이게 할 것이다.')
print('이것은 두 줄이지만\
 한 줄처럼 보이게 할 것이다.')