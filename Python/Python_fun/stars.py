def draw_stars():
    a = [2,4,10,16]
    for i in range(len(a)):
        c = a[i] * '*'
        print c

draw_stars()


def draw_stars(arr):
    for i in arr:
        if isinstance(i, int):
            print "*"*i
        elif isinstance(i, str):
            print i[0]*len(i)

draw_stars([1,2,3,"hello",5,4,"world","olie olie oxen freeee!",1])
