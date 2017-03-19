# 사용자에게 가위, 바위, 보 중 하나 묻기
# 컴퓨터도 같이 가위, 바위, 보를 내고 승패를 가름
# 다합쳐 3번을 지거나, 3번을 이기면 게임은 최종 스코어를 보여 주면서 끝

b = input("가위, 바위, 보 중 하나를 내시오.")
import random
a_List = ["가위", "바위", "보"]
print(random.choice(a_List))

if a_List == b:
    print("비겼습니다.")

elif (a_List == "가위" and b == "보") or    \
     (a_List == "바위" and b == "가위") or   \
     (a_List == "보" and b == "바위"):
     print("이겼습니다.")

else:
    print("졌습니다.")
