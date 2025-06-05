#task3, https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
def minion_game(string):
    # your code goes here
    S = string.upper()
    all_words = []

    for i in range(len(S)):
        for j in range(i+1,len(S)+1):
            all_words.append(S[i:j])

    vowels = ['A','E','I','O','U']
    score_count = 0

    for vowel in all_words:
        if vowel[0] in vowels:
            score_count+=1
    
    vscore = score_count
    score_count=0

    for consonant in all_words:
        if consonant[0] not in vowels:
            score_count+=1
    cscore = score_count
    
    if vscore > cscore:
        print("Kevin", vscore)
    elif vscore < cscore:
        print("Stuart", cscore)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)