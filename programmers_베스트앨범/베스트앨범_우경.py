import operator
from collections import defaultdict

class Music:
    def __init__(self, num, genre, play) :
        self.num = num
        self.genre = genre
        self.play = play

def solution(genres, plays):
    answer = []
    db = []
    g_db = defaultdict(int)
    
    for i in range(len(genres)):
        db.append(Music(i, genres[i], plays[i]))
        g_db[genres[i]] += plays[i]
    
    db.sort(key=operator.attrgetter("play"), reverse=True)
    g_db = sorted(g_db, key = lambda k:g_db[k], reverse=True)
    
    
    for g in g_db:
        idx = 0
        cnt = 0
        while cnt <2:
            if idx >= len(db):
                break
            if db[idx].genre == g:
                answer.append(db[idx].num)
                cnt += 1
            idx += 1
    
    return answer