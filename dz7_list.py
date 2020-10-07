
import os
import logging

logging.basicConfig(level=logging.INFO,
                    filename="app_test3.log",
                    filemode="w")

filelist = os.listdir('.')
logging.info(f' Filelist :, {filelist}')

