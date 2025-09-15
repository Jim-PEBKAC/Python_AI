class Robot:

    # 생성자(?) : 객체화할 때 호출되는 함수의 일종
    # 객체화가 될 때 가장 먼저 호출된다.
    def __init__(self):
        print('Robot이 복사될 때 제일 먼저 호출되는 멤버')

    def doit(self):
        print(f'나는 Robot의 함수 입니다.')

robot = Robot()
robot.doit()