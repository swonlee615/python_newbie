# passenger 승객 : 1~50명
# ridetime 운행 소요시간 : 5분~50분
# condition 내 조건 : 5~15분

import random

passenger = range(1, 51)

ridetime = list(range(5, 51))

realp = 0

for i in passenger:
    random.shuffle(ridetime)
    if 5 <= ridetime[0] < 16:
        ride = "[O]"
        realp += 1
    else:
        ride = "[ ]"
    print(ride, i, "번째 손님", "(소요시간 : {}분)".format(ridetime[0]))


print("총 탑승 승객 : {}분".format(realp))