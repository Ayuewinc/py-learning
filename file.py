from math import sqrt
def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False

if __name__ == '__main__':
    fa=open('a.txt', 'w', encoding='utf-8')
    fb=open('b.txt', 'w', encoding='utf-8')
    fc=open('c.txt', 'w', encoding='utf-8')
    for n in range(1, 10000):
        if is_prime(n):
            if n < 100:
                fa.write(str(n) + '\n')
            elif n < 1000:
                fb.write(str(n) + '\n')
            else:
                fc.write(str(n) + '\n')
    fa.close()
    fb.close()
    fc.close()

    with open('a.txt', 'r') as fa:
        print(fa.read())
    with open('b.txt', 'r') as fb:
        print(fb.read())
    with open('c.txt', 'r') as fc:
        print(fc.read())

