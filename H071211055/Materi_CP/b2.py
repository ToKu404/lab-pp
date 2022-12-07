n = int(input())
stick = list(map(int, input().rstrip().split()))

while len(stick):
    print(len(stick))
    stick2 = []
    
    for i in stick:
        stick2.append(i - min(stick))
    # stick = [i - min(stick) for i in stick]
    stick = stick2
    c = min(stick)
    for j in range(stick.count(c)):
        stick.remove(c)
