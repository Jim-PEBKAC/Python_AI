#for 반복문은 반복 횟수가 정해진 상태에 적합하다.

#물 10잔 떠오기
#for [하나씩 가져올 변수] in [범위]:
for cup in range(1,11): #1부터 10까지
    print(f'물{cup} 번째 잔 떠왔습니다.')
    for cof in range(1,3) :
        print(f'커피 믹스{cof}개 넣었습니다.')
    print(f'커피 {cup}번째 잔이 만들어졌습니다.')
    # 1은 작거나 같다를 의미, 10은 작다를 의미하기 때문에 11을 넣어야 맞음. (1:11)=1~10
    # (개발자의 숫자는 0부터 (0=1))
    
print()
# 만약 커피를 타는데 한 잔의 물에 믹스 커피 두 개씩 넣어야한다면
# 반복문 안에 반복문이 발생한다. -> 이중 for문


# 강사님 작성 내용 -> 삼중 for문
for cup in range(1, 11):
    print(f'물 {cup} 번째 잔 떠왔습니다.')
    for mix in range(1,3):
        print(f'{mix} 번째 믹스를 넣는다.')
        for spoon in range(1,4):
            print(f'{spoon} 번 젓는다.')
    print(f'커피 {cup}번째 잔이 만들어졌습니다.') # 이건 내가 넣은 거