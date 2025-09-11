cup = 0
running = True

# while running:
#     cup += 1
#     print(cup)
#     if cup == 10:
#         # running = False
#         break
# print('while 문 종료')

# 조건 뒤에 : 붙이는 거 잊지말기

n=1 # 먼저 변수 n을 1로 설정
for i in range(1,10):
    # if i ==3 or i ==6 or i ==9: *or문법 사용
    # if 1 % 3 == 0: *내가 생각못한 부분, '3으로 남고 나머지가 0이면 넘긴다.'를 의미

    if i == 3*(n+1): #3의 배수를 변수 설정
        n=n+1 #3의 배수를 한 번이 아닌 여러번 하기 위해 변수 설정
        continue
    print(i)
