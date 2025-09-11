import random

number = random.randint(1,31) # 1에서 31까지 랜덤한 숫자를 number에 대입해라.
print(f'내 마음속 숫자: {number}') # 그 랜덤한 숫자 number를 출력해라.
running = True # True를 running에 대입해라.

while running: # True이면 무한 루프 / while은 오른쪽에 있는 조건 결과가 True일 경우 반복되는 조건문, 처음부터 True라서 무한루프임. 멈추려면 False 필요
    # 입력된 값을 정수(int)로 변환해 guess에 대입해라
    guess = int(input('1~31 중 내가 생각한 숫자는?')) # 외부에서의 입력 값을 정수로 바꿔라
    print(f'입력받은 숫자: {guess}') # 외부에서 입력한 정수 값을 출력해라.

    if guess == number: # 만약 입력 값이 랜덤한 숫자와 같다면
        running = False # running에 False을 대입해라. -> True에서 False으로 바뀌었기 때문에 while은 멈추게 된다.
        print(f'{guess}는 정답 입니다.') # 입력 값은 정답이라고 출력해라

    elif guess < 1 or guess > 31: ##이걸 뒤에 넣으면 작동 안함. (1차 필터의 위치를 정밀 필터자리에 끼운거나 마찬가지이기 때문)
        print('알맞은 숫자를 입력해주세요.') # 만약 입력 값이 1보다 작거나 31보다 크다면 외부 값을 다시 요청해라.

    elif guess < number : # 만약 입력 값이 number보다 작으면
        print(f'{guess}는 내가 생각한 숫자보다 작습니다.') # 작다고 출력해라

    elif guess > number: # 만약 입력 값이 number보다 크다면
        print(f'{guess}는 내가 생각한 숫자보다 큽니다') # 크다고 출력해라



# 강사님 코드
