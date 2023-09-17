# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

height = input("키를 입력해주세요 ")
gender = input("성별을 입력해주세요 ")

def std_weight (height, gender):
    height = float(height)
    if gender == "여성" :
        std_weight = (height * 0.01) * (height * 0.01) * 21 #키에 0.1 곱하고 전체 2제곱!
    else :
        std_weight = (height * 0.01) * (height * 0.01) * 22
    print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(int(height), gender, round(std_weight, 2)))

std_weight(height, gender)

#결과
#키를 입력해주세요 175
#성별을 입력해주세요 남성
#키 175cm 남성의 표준 체중은 67.38kg 입니다.