import sys

range = xrange if (sys.version_info.major == 2) else range

def feeder(lst, count=None):
    '''generator that yields pairs for computation'''

    # use count if provided else find length of list
    count = count or len(lst)

    if count < 2:
        yield (0,0)
    else:
        #for i in range(count):
        #    for j in range(i+1, count):
        #        yield (lst[i], lst[j])

        outer_iter = iter(lst)
        c = 0
        for o in outer_iter:
            c += 1
            inner_iter = iter(lst[c:])
            for i in inner_iter:
                yield (o, i)



def find_largest_loss(lst, count=None):

    largest_loss = None

    for n1, n2 in feeder(lst, count):
        loss = n2 - n1
        #print('%d - %d = %d' % (n2,n1,loss))
        if largest_loss is None or loss < largest_loss:
            largest_loss = loss;

    return largest_loss