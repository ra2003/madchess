def isObtuse(square1, square2):
    x1, y1 = square1
    x2, y2 = square2

    m = x1 - x2
    n = y1 - y2

    if m == n:
        return True

    return False

def isAcute(square1, square2):
    x1, y1 = square1
    x2, y2 = square2

    m = x1 - x2
    n = y1 - y2

    if m == -n:
        return True

    return False



def isVertical(square1, square2):
    x1, y1 = square1
    y2, y2 = square2

    if y1 == y2:
        return True

    return False

def isHorizontal(square1, square2):
    x1, y1 = square1
    x2, y2 = square2

    if x1 == x2:
        return True

    return False
    pass

def minOnLeft(square):
    x, y = square
    no = (x, y)

    for ind in xrange(8):
        x = x - 1
        y = y - 1

        if x >= 0 and y >= 0:
            no = (x, y)
        else:
            return no

def minOnRight(square):
    x, y = square
    no = (x, y)

    for ind in xrange(8):
        x = x - 1
        y = y + 1

        if x >= 0 and y <= 7:
            no = (x, y)
        else:
            return no

def isOnLeft(square):
    x, y = minOnLeft(square)

    for ind in xrange(8):
        if x <= 7 and y <= 7:
            yield((x, y))

        x = x + 1
        y = y + 1


def isOnRight(square):
    x, y = minOnRight(square)

    for ind in xrange(8):
        if x <= 7 and y >= 0:
            yield((x, y))

        x = x + 1
        y = y - 1

def minOnVertical(square):
    x, y = square
    return (0, y)


def minOnHorizontal(square):
    x, y = square
    return (x, 0)

def isOnVertical(square):
    x, y = minOnVertical(square)

    for ind in xrange(8):
        if x <= 7:
            yield((x, y))

        x = x + 1


def isOnHorizontal(square):
    x, y = minOnHorizontal(square)

    for ind in xrange(8):
        if y <= 7:
            yield((x, y))

        y = y + 1


def edge(square):
    x, y = square

    data = []

    m, n = x - 1, y - 1

    data.append((m, n))

    m, n = x - 1, y + 1
    data.append((m, n))

    m, n = x - 1, y
    data.append((m, n))

    m, n = x + 1, y - 1
    data.append((m, n))

    m, n = x + 1, y + 1
    data.append((m, n))

    m, n = x + 1, y
    data.append((m, n))

    m, n = x, y - 1
    data.append((m, n))

    m, n = x, y + 1
    data.append((m, n))

    for m, n in data:
        if m >= 0 and n >= 0 and m <= 7 and n <= 7:
            yield((m, n))


def vertice(square):
    x, y = square

    data = []

    m, n = x - 2, y - 1

    data.append((m, n))
    m, n = x - 2, y + 1
    data.append((m, n))


    m, n = x + 2, y - 1
    data.append((m, n))

    m, n = x + 2, y + 1
    data.append((m, n))

    m, n = x - 1, y - 2

    data.append((m, n))
    m, n = x + 1, y - 2

    data.append((m, n))
    m, n = x - 1, y + 2

    data.append((m, n))
    m, n = x + 1, y + 2
    data.append((m, n))

    for m, n in data:
        if m >= 0 and n >= 0 and m <= 7 and n <= 7:
            yield((m, n))


def isOnBoard(square):
    x, y = square

    if x >= 0 and y >= 0 and x <= 7 and y <= 7:
        return True
    return False

def goOnRight(square1, square2):
    x, y = square1 if square1 < square2 else square2

    xm, ym = square1 if square1 > square2 else square2

    for ind in xrange(0, 8):
        x = x + 1
        y = y - 1
      
        if x >= xm or y <= ym:
            break
        """
        if (x, y) == (xm, ym):
            break
        """

        yield((x, y))


def goOnLeft(square1, square2):
    x, y = square1 if square1 < square2 else square2

    xm, ym = square1 if square1 > square2 else square2

    for ind in xrange(0, 8):
        x = x + 1
        y = y + 1
       
        if x >= xm or y >= ym:
            break
        """
        if (x, y) == (xm, ym):
            break
        """
        yield((x, y))

def goOnVertical(square1, square2):
    x, y = square1 if square1 < square2 else square2

    xm, ym = square1 if square1 > square2 else square2

    for ind in xrange(0, 8):
       
        x = x + 1

        if x >= xm:
            break

        yield((x, y))


def goOnHorizontal(square1, square2):
    x, y = square1 if square1 < square2 else square2

    xm, ym = square1 if square1 > square2 else square2

    for ind in xrange(0, 8):
        y = y + 1
       
        if y >= ym:
            break

        yield((x, y))

def hands(square):
    x, y = square
    
    if y - 1 >= 0:
        yield((x, y - 1))

    if y + 1 <= 7:
        yield((x, y + 1))

def arrow(side, square):
    x, y = square

    data = []

    m, n = x + side, y - 1
    data.append((m, n))

    m, n = x + side, y + 1
    data.append((m, n))

    m, n = x + side, y

    data.append((m, n))
    m, n = x + 2 * side, y
    data.append((m, n))

    for m, n in data:
        if m >= 0 and n >= 0 and m <= 7 and n <= 7:
            yield((m, n))


