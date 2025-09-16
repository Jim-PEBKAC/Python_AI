class Runner:
    def run(self):
        print(f'달린다.')

    def sprint(self):
        print(f'전력질주를 한다.')


class Jumper:
    def jump(self):
        print(f'점프를 한다.')

    def high_jump(self):
        print(f'높이 점프를 한다.')

class Person(Jumper, Runner): # Jumper와 Runner를 상속 받았다.
    def walk(self):
        print(f'걷는다.')

# walk() 함수를 사용하기 위해서는 먼저 Person 클래스를 객체화한다.
# Person 클래스 안에 Jumpoer와 Runner을 상속했기 때문에 그 안에 함수도 사용 가능하다.
p=Person()
p.walk()
p.high_jump()
p.jump()
p.sprint()
p.run()


# 상속받은 함수들을 내것처럼(객체로부터) 사용한다.
# 상속을 받으면 좋은점 1. 객체 입장에서는 기능이 늘어난다.
# 상속을 받으면 좋은점 2. 사용자 입장에서는 하나의 객체화로 여러 기능을 사용 할 수 있다.