
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
    integers = []
    snowflakes = []
    for _ in range(n):
        snowflakes.append(list(map(int, input().split())))


    print(find_identical_snowflakes(snowflakes))
    
