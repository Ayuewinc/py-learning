if __name__ == '__main__':
    with open('a.jpeg', 'rb') as fb1:
        data = fb1.read()
    with open('b.jpeg', 'wb') as fb2:
        fb2.write(data)