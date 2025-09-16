# try:
#     text=input('값을 넣으면 숫자로 변환됩니다.')
#     num = int(text)
#     print(f'당신이 입력한 값 : {num}이 숫자로 변환 되었습니다.')
#
#
# except Exception as e:  # 예외의 최상위 부모이기 때문에 다른 자식 예외들이 모두 들어올 수 있다.
#     print('제대로 된 값을 입력하세요.')

while True:
    try:
        text=input('값을 넣으면 숫자로 변환됩니다.')
        num = int(text)
        print(f'당신이 입력한 값 : {num}이 숫자로 변환 되었습니다.')
        break
    except ValueError:
        print(f'{text}는 숫자가 아닙니다.')