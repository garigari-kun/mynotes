
def complexity_with_break_statement(n):
    count = 0
    for i in range(int(n / 2), n):
        j = 1
        while j + n / 2 <= n:
            break
            j = j * 2
    print(count)

if __name__ == '__main__':
    complexity_with_break_statement(20)
