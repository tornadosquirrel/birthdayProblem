from random import randint

cnt = 0  # 카운트
num = int(input("사람 몇명? "))

if 0 < num < 367:  # 방지용 코드
    re = int(input("반복 횟수? "))
    if re > 0:  # 방지용 코드
        for _ in range(re):  # re번 반복
            li = [randint(1, 366) for _ in range(num)]  # num명 뽑기
            if len(li) != len(set(li)):  # 중복된 숫자가 존재하는가?
                cnt += 1  # 카운트 올리기
        print(f"{num}명으로 이루어진 {re}개 그룹에서 같은 생일을 가진 사람들이 존재하는 그룹은 {cnt}개입니다.")
    else:
        print("올바른 반복 횟수를 입력하세요.")
else:
    print("올바른 인원 수를 입력하세요.")
