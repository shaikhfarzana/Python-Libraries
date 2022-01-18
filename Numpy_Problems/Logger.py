"""
@Author: Farzana Shaikh
@Date: 18-01-2022 04:00PM
@Last Modified by: Farzana Shaikh
@Last Modified time: 18-01-2022 04:00PM
@Title : Program for creating object of logger.
"""

import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('Numpy_file.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

