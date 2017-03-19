# 학교 클래스 만들기_이름, 설립연도, 주소 활성화

class University:
    def __init__(self, name, year, address):
        self.name = name
        self.year = year
        self.address = address

university1 = University("서울대학교", "1987", "서울시 관악구")

print(university1.name)
print(university1.year)
print(university1.address)
