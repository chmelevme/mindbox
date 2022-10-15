from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('n_customers', type=int, nargs=1,
                    help='an integer for the number of clients')
parser.add_argument('n_first_id', type=int, nargs='?', default=0,
                    help='an integer for the number of first client id')


def calc_groups_coutn(n_customers: int, n_first_id: int = 0):
    res = {}
    assert n_customers > 0
    assert n_first_id > 0 

    for i in range(n_first_id, n_first_id + n_customers):
        num = sum(map(int, list(str(i))))
        if num not in res:
            res[num] = 1
        else:
            res[num] += 1
    print(res)
    return res


if __name__ == '__main__':
    args = parser.parse_args()
    calc_groups_coutn(args.n_customers[0], args.n_first_id)
