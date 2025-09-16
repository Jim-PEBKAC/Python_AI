class Car:
    gear = 0
    on = False

    # 생성자 - 클래스 사용 시 객체화를 하기 때문에 필수로 생성해야한다.
    # 그런데 프로그래밍의 규칙 중 하나는 너무 당연히 있어야할 것들은 생략 가능하다.
    def __init__(self):
        # 혹시나 기어가 들어가있거나 시동이 켜져있을 수 있어 초기 상태로 되돌려 놓는다.
        self.gear = 0
        self.on = False

    # 멤버 함수 - 클래스 안의 생성자 함수들은 해당 객체를 표시하기 위한 self를 기본으로 갖고 있다.
    def start(self):
        if self.on == False:
            print(f'시동이 걸렸습니다.')
            self.on = True
        else:
            print(f'시동이 이미 걸려있습니다.')
    def change(self)
        print(f'{self.gear}단으로 변속했습니다.')
        self.gear += gear