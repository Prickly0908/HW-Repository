import logging
import math
import argparse
import json


class Quadratic1:
    def __init__(self, a, b, c):

        self.a = a
        self.b = b
        self.c = c

    logging.basicConfig(level=logging.DEBUG,
                        filename='app_test22.log',
                        filemode="w")

    def discriminant(self):
            d = math.pow(self.b, 2) - 4 * self.a * self.c
            if d > 0:
                logging.info(f'discriminant={d}')
            else:
                logging.info(f'discriminant={d}')
                d = None
                logging.info('D<0')

            return d


    def get_roots(self, d):

        if d != None:
            x1 = float((-1) * self.b + math.sqrt(d) / (2 * self.a))
            x2 = float((-1) * self.b - math.sqrt(d) / (2 * self.a))
            logging.info((f'x1:{x1} x2:{x2}'))
            logging.info("Roots calculation. Program is done")
        else:
            x1 = None
            x2 = None


        return x1, x2