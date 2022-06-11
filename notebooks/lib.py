""" some definitions
"""

import os

DATA_DIRECTORY = os.path.join('.','..','data')

RAW_DATA_DIRECTORY = os.path.join(DATA_DIRECTORY, 'raw')
DATA_DICTIONARY_PATH = os.path.join(RAW_DATA_DIRECTORY, 'Interview2_DataChallenge_DataDictionary.csv')
USER_DATA_RAW_PATH = os.path.join(RAW_DATA_DIRECTORY, 'Interview2_DataChallenge.csv')

INTERIM_DATA_DIRECTORY = os.path.join(DATA_DIRECTORY, 'interim')
USER_DATA_PATH = os.path.join(INTERIM_DATA_DIRECTORY, 'Interview2_DataChallenge.pkl')