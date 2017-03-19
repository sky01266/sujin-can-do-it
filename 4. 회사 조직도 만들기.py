# 사람 클래스(이름, 나이, 성별)
# 사람 클래스의 상속으로 직장 클래스를 만들자. 추가 사항은 직급(대리)

class People:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# people1 = People("정정열", "45", "남")
# people2 = People("이지원", "25", "여")
# people3 = People("심지혜", "30", "여")

# inheritance
class Position(People):
    source = "대리"

position = Position("정정열", "45", "남")
print(position.name)
print(position.age)
print(position.gender)
print(position.source)
