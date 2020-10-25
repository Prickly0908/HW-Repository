import argparse
from quadratic_args import Quadratic1


def parse_args():
    parser = argparse.ArgumentParser(
        description='Simple input for quadratic equation Ax^2 + Bx + C = 0')

    parser.add_argument('--a', type=float, required=True,
                        help='Coefficient A')
    parser.add_argument('--b', type=float, required=True,
                        help='Coefficient B')
    parser.add_argument('--c', type=float, required=True,
                        help='Coefficient C')

    return parser.parse_args()


def run(a,b,c):
    qe = Quadratic1(a=a, b=b, c=c)
    d = qe.discriminant()
    x1, x2 = qe.get_roots(d)
    return x1,x2

if __name__ == "__main__":
    args = parse_args()
    x1, x2 = run(a=args.a, b=args.b, c=args.c)