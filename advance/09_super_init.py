class Parent():
    def __init__(self):
        print(f'부모 생성자 실행')

class Child(Parent):
    def __init__(self):
        super().__init__() # 생략된 부모 생성자
        print(f'자식생성자')

ch = Child()

