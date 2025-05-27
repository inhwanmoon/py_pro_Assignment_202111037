import os
import pickle

def input_scores():
    s = []
    i = 1
    while True:
        n = int(input(f'#{i}? '))
        if n < 0:
            break
        s.append(n)
        i += 1
    return s

def get_average(s):
    if not s:
        return 0.0
    total = 0
    for n in s:
        total += n
    return total / len(s)

def show_scores(s):
    for n in s:
        print(n, end=' ')
    print()

def save_scores(scores, filename='score.bin'):
    with open(filename, 'wb') as file:
        pickle.dump(scores, file)

def load_scores(filename='score.bin'):
    if not os.path.exists(filename):
        return None
    with open(filename, 'rb') as file:
        scores = pickle.load(file)
    return scores

FILE_NAME = 'score.bin'
scores = None

loaded_scores = load_scores(FILE_NAME)

if loaded_scores is not None:
    scores = loaded_scores
    print('\n[파일 읽기]') 
else:
    print('[점수 입력]') 
    scores = input_scores()

print('\n[점수 출력]') 
print('개인점수: ', end='') 
show_scores(scores)

avg = get_average(scores)
print(f'평균: {avg:.1f}') 

save_scores(scores, FILE_NAME)
