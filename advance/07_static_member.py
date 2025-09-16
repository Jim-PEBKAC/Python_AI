class Robot:
    count = 0

    def how_count(self):
        print(f'객체 메서드: {self.count}')

    @classmethod # 원본 영역의 변수를 건드릴 수 있다는 표시
    def std_count(self):
        print(f'클래스 메서드 : {self.count}')

r1 = Robot()
r2= Robot()
# r1과 r2는 다른 객체라 count를 건드렸을 때 서로 영향받지 않는다.
r1.count += 1
print(f'r1.count : {r1.count}')
print(f'r2.count : {r2.count}')
r2.count = 100
print(f'r1.count : {r1.count}')
print(f'r2.count : {r2.count}')

# 원본의 내용을 고치고 싶으면 원본으로 직접 가야한다.
Robot.count = 1000

print(f'원본 수정하고 일전에 생성했던 객체(복사본)는 당연히 변하지 않음')
print(f'r1.count : {r1.count}')
print(f'r2.count : {r2.count}')
r1.how_count()
r2.how_count()

# 마찬가지로 원본의 내용을 확인하고 싶다면 원본 영역으로 가면된다.
print(f'원본 count : {Robot.count}')
Robot.std_count()

print(f'원본 수정하고 객체를 다시 생성했을 때')
# 원본을 수정한 뒤 객체를 생성했을 때(복사) 영향 받은 것을 확인할 수 있다.
r1 = Robot()
r2= Robot()


r1.count += 1


print(f'r1.count : {r1.count}')
print(f'r2.count : {r2.count}')
r2.count = 1005
print(f'r1.count : {r1.count}')
print(f'r2.count : {r2.count}')

