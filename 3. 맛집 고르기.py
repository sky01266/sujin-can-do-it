# 1) 한식, 중식, 일식 중 한 가지를 고르라는 명령어를 제시
# 2) 그 중 한 가지를 고르면 식당 이름을 하나로 임의로 추천_list 사용

# 1) 명령어 입력
a = input("한식, 중식, 일식 중 한 가지를 고르세요.")

import random
if a == "한식":
    a_List = ["돼지 불백집", "소불고기집", "김치찜"]
    print(random.choice(a_List))

if a == "중식":
    a_List = ["진짜루", "왕서방", "불짬뽕"]
    print(random.choice(a_List))

if a == "일식":
    a_List = ["미소야", "전통 라멘집", "가츠마루"]
    print(random.choice(a_List))
