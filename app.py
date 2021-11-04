#타자연습 게임

import random
import time

words = [] # 영어 단어 리스트 (1000개 로드하기)

n = 1   #게임 시도 횟수
correct_cnt = 0 #정답 개수

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())
    
# print(words)    #단어 리스트 확인

input("Ready? Press Enter Key!")

start = time.time()

while n <= 5:
    random.shuffle(words)
    q = random.choice(words)
    print()

    print("*Question # {}".format(n))
    print(q) #문제 출력

    x = input() #타이핑 입력

    print()
    if str(q).strip() == str(x).strip(): #입력한 답이 정답이라면
        print("Pass!")        
        correct_cnt += 1
    else:
        print("Wrong!")

    n += 1
    
end = time.time() #끝난 시간 기록
playtime = end - start #플레이 시간
playtime = format(playtime, ".2f")

print()

if correct_cnt >= 3:
    print("합격")
else:
    print("불합격")

print()

#수행시간 출력
print("게임 시간 : ", playtime, "초", " 정답 개수 : {}".format(correct_cnt))

#시작 지점
if __name__ == '__main__':
    pass