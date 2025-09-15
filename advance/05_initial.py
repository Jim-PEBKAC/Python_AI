class Puppy:

    name=""  # 멤버 변수(필드): class 안에서 사용 가능한 변수
    goal=""  # 마찬가지

    def __init__(self,name,goal): # 생성자: 객체화시 호출되는 함수(초기값)
        self.name=name
        self.goal=goal

puppy = Puppy("멍멍이","집지키기")

