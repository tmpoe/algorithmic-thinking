
def what_letters_to_delete(a, b):
    if len(a) < len(b) or len(a) == len(b):
        return 0
    solutions = []
    for i, c in enumerate(a):
        if c != b[i]:
            solutions.append(i)

            for j in reversed(range(0, i)):
                if a[j] == c:
                    solutions.append(j)
                else:
                    break
        if solutions:
            break
    
    return solutions if solutions else 0

if __name__ == '__main__':
    print(what_letters_to_delete('abbbc', 'abc'))