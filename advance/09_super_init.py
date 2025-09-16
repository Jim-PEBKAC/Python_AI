class Parent():
    def __init__(self):
        print(f'부모 생성자 실행')

class Child(Parent):
    def __init__(self):
        super().__init__() # 생략된 부모 생성자
        print(f'자식생성자')

ch = Child()

# 부모가 초기화가 필요하다면 자식에게 값을 전달해서 자식이 부모에게 전달하도록 한다.
class SchoolMember():

    name = ''
    age = 0

    def __init__(self, name, age): # 3. 받아온 값을 초기화하고 객체화된다.
        self.name = name
        self.age = age

class Teacher(SchoolMember):
    salary = 0

    def __init__(self, name, age, salary):
        super().__init__(name, age) # 2. 부모 초기화 먼저 실행 후 값 전달
        self.salary = salary # 4. 그리고 내가 초기화하면서 객체화

# 1. Teacher 라는 클래스를 객체화한다.(초기화를 위해 매개변수를 전달)
t=Teacher('김철수',33,5000000)
# 5. name과 age는 부모것이지만 내것처럼 내 객체에서 쓸 수 있게 된다.
print(f'{t.name}({t.age})-{t.salary}원')