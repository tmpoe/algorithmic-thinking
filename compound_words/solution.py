import time
from pathlib import Path
from collections import OrderedDict
MAX_NUM_WORDS = 120000

if __name__ == '__main__':

    with open((Path(__file__).parent.joinpath('input.txt'))) as f:
        n = int(f.readline())
        words = OrderedDict()
        for _ in range(n):
            words[f.readline().strip()] = 1
            if len(words) > MAX_NUM_WORDS:
                break

        print("***** Finding compounds *****")
        start = time.time()
        for word in words:
            for i in range(1, len(word)):
                if word[:i] in words and word[i:] in words:
                    print(word)
                    break

        end = time.time()
        print("Elapsed time", end - start)