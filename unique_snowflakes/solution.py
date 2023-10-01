
from collections import defaultdict

MAX_SNOWFLAKE_SIZE = 10**6

def find_identical_snowflakes(snowflakes):
    print(snowflakes)
    for i in range(len(snowflakes)):
        for j in range(i+1, len(snowflakes)):
            if len(snowflakes[i]) == len(snowflakes[j]):
                for k in range(len(snowflakes[i])):
                    if (_identical_right(snowflakes[i], snowflakes[j], k) or _identical_left(snowflakes[i],snowflakes[j], k)):
                        return True
    return False

def _identical_right(s1, s2, start):
    for offset in range(len(s1)):
        if s1[(start + offset) % len(s1)] != s2[offset]:
            return False
    return True


def _identical_left(s1, s2, start):
    for offset in reversed(range(len(s1))):
        if s1[(start - offset) % len(s1)] != s2[offset]:
            return False
    return True


if __name__ == '__main__':
    n = int(input())
    snowflakes = defaultdict(list)
    for _ in range(n):
        s = list(map(int, input().split()))
        snowflakes[sum(s) % MAX_SNOWFLAKE_SIZE].append(s)

    found = False
    for similar in snowflakes.values():
        if find_identical_snowflakes(similar):
            print("Identicals found")
            found = True
            break

    if not found:
        print("No identicals found")
    
