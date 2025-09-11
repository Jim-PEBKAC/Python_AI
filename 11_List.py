# 파스칼표기법: 맨 앞글자만 대문자(Java의 class 생성시 사용)
# 카멜표기법: 단어에 의미가 있는 첫 글자를 대문자로 한다. ex) blackColor, dfList ...
# 스네이크 표기법(Python 주로 사용): 단어간 구분을 _로 한다. ex) black_color, df_list
# list와 상관없는 내용이지만 추후에 필요


# list 생성 방법1 : 빈 리스트 생성
a = []

# list 생성 방법2 : 값이 있는 리스트 생성
df_list=['apple','mango', 'carrot','banana']

print(f'shop_list: {df_list}') #f-string 사용한 이유는 성의있어 보이기 위함. 굳이 사용안해도 됌.
print(df_list[1:2]) # 첫 번째 가로열에서 두 번째 세로열에 있는 거 출력해.

# [리스트에 값 넣는 방법]
# 가장 뒤로부터 넣는 방법 (순서대로 넣는다. → 줄 세우는 구조)
a.append(1)
a.append(2)
a.append(3)

# 특정한 번호를 지정해서 넣는 방법
a.insert(0,'x') # 기존 첫 번째를 뒤로 밀고 들어간다.
a.insert(1,'z') # 기존 두 번째를 뒤로 밀고 들어간다.
print(f'a:{a}')

print(f'a의 리스트의 개수: {len(a)}') #len은 길이를 반환하는 함수인데 리스트에서는 원소 개수를 뜻함
#a의 3번째의 값
print(f'a[2]={a[2]}')
#a의 가장 마지막에 있는 값
print(f'a[4]={a[4]}') # print(a[4]) {}가 있는 이유는
# a리스트 가로열의 5번째는 3이라는 원소가 있음. 그리고 그건 a는 변수이기 때문에 감싸줘야함
print(a[4]) # f-string 사용 안하면 간단히 표기 가능하지만 되도록 사용할 수 있도록

# 강사님 코드
print(f'a의 마지막 방의 값={a[4]}')
print(f'adml 마지막 방의 값={a[len(a)-1]}')
print(f'a의 마지막 방의 값={a[-1]}')

# 리스트 정렬
# .sort: 정렬된 이후 원본 변경됌
# .sorted: 정렬 후 복사본을 만들어 보여줌. 원본 훼손 안됌.
df_list.sort() # 오름차순
print(f'df_list:{df_list}')

df_list.sort(reverse=True) # 내림차순
print(f'df_list:{df_list}')

print(f'df_list:{df_list}')

# a의 2번 인덱스에 c를 넣는다.
a[2]='c' # insert와 다르게 3번째 값을 지우고 c가 들어간다.
print(f'a:{a}') # 기존 list에서 3번째 값인 1이 삭제되고 c가 들어간 것을 확인 가능

#list 삭제 방법
del a[2] # 리스트 세 번째 값을 제거
print(f'a:{a}') # 세 번째 c가 사라진 걸 확인할 수 있음.