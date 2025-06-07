#task3, https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
def minion_game(string):
    S = string.upper()
    n = len(S)
    kevin_score = 0
    stuart_score = 0
    vowels = 'AEIOU'

    for i in range(n):
        if S[i] in vowels:
            kevin_score += (n - i)
        else:
            stuart_score += (n - i)

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
  s = input()
  minion_game(s)