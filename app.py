#타자연습 게임

import random
import time

#사운드 출력 모듈
# import pygame
import sqlite3
import datetime

# pygame.mixer.init()
# correct_sound = pygame.mixer.Sound("./sound/good.wav")
# #correct_sound.set_volume(0.5)
# correct_sound.play()

#DB생성 & Auto Commit
conn = sqlite3.connect('/mnt/c/Users/mch12/Documents/typingGame/resource/record.db', isolation_level=None)
# 커서 연결
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, correct_cnt INTEGER, record text, regdate text)")

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
        #정답 소리 재생

        correct_cnt += 1
    else:
        print("Wrong!")
        #오답 소리 재생

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

#기록 DB삽입
cursor.execute("INSERT INTO records('correct_cnt', 'record', 'regdate') VALUES(?,?,?)", (correct_cnt, playtime, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


#수행시간 출력
print("게임 시간 : ", playtime, "초", " 정답 개수 : {}".format(correct_cnt))

#시작 지점
if __name__ == '__main__':
    pass