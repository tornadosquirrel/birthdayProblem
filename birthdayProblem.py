from random import * #랜덤모듈

li = [] #사람 23명
cnt = 0 #카운트
num = int(input("사람 몇명?"))

if num < 367 and num > 0: #방지용코드
    re = int(input("반복 횟수?"))
    if re > 0: #방지용코드
        for i in range(re): #re번 반복
            for i in range(num): #num명 뽑기
                li.append(randint(1, 366)) #윤년의 첫째날부터 마지막날까지중에 뽑아서 넣기
            if len(li) != len(set(li)): #중복된 숫자가 존재하는가?(set함수는 중복을 무시함)
                cnt += 1 #카운트 올리기
                li = [] #리스트 초기화
        print(f"{num}명으로 이루어진 {re}개 그룹에서 같은 생일을 가진 사람들이 존재하는 그룹은 {cnt}개입니다.")
    else:
        print("멍청한새끼야")
else:
    print("멍청한새끼야")