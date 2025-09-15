# 코드 리뷰 및 의견 쓰는 주석

int=123 # 정수
float=3.14 # 실수
octal = 0o117 #8진수(숫자0과 알파벳o를 추가)
hex = 0x8ff #16진수 (숫자0과 알파벳x를 추가)

# print('int : 'int) # 문자 + 숫자는 출력하지 않는다.
# f-string을 사용하면 문자열과 다른 타입의 데이터를 합께 출력할 수 있다.
print(f'int: {int}') # {}안에 내용은 보존하라는 의미를 갖는다.
print(f'float:', float)
print(f'octal:', octal)
print(f'hex:', hex)
