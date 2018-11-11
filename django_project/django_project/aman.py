if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        x = input()
        y = x.split(' ')
        z = list()
        if(y[0] == 'insert'):
            z.insert(int(y[1]), y[2])
        elif(y[0] == 'remove'):
            z.remove(int(y[1]))
        elif(y[0] == 'append'):
            z.append(y[1])
        elif(y[0] == 'sort'):
            z.sort()
        elif(y[0] == 'pop'):
            z.pop()
        elif(y[0] == 'reverse'):
            z.reverse()
        elif(y[0] == 'print'):
            print(z)
