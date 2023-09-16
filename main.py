from datetime import datetime
from threading import Thread, Lock

G_LOCK = Lock()

a = list(range(1, 4000, 3))
b = list(range(4, 6000, 4))
res = []


def _sum(n1, n2):
    return (n1 ** 6) * n2


def worker(x, y, result: list):
    _res = _sum(x, y)
    with G_LOCK:
        result.append(_res)


def main_t():
    workers = [Thread(target=worker, args=(a1, b1, res)) for a1, b1 in zip(a, b)]
    for w in workers:
        w.start()

    for w in workers:
        w.join()

    print(res)


def main():
    res = []
    for a1, b1 in zip(a, b):
        res.append(a1 ** 3 * b1)
    print(res)


if __name__ == '__main__':
    # print(len(a), len(b))
    start = datetime.now()
    main_t()
    print(datetime.now() - start)


    start = datetime.now()
    main()
    print(datetime.now() - start)
