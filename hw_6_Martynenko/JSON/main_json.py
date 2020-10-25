import argparse
from quadratic_json import Quadratic


def parse_args():
    parser = argparse.ArgumentParser(description='Simple input for quadratic equation Ax^2 + Bx + C = 0')
    parser.add_argument('--path', type=str, required=True, help='Path to config .json')
    return parser.parse_args()

def run(path):
    qe = Quadratic(path_config=path)
    d = qe.discriminant()
    x1, x2 = qe.get_roots(d)
    return x1,x2

if __name__ == "__main__":
    args = parse_args()
    x1, x2 = run(path=args.path)