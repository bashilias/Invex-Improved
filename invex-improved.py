'''
    Invex-Improved v0.1 (beta) by 1LIA5

    Original Invex written by steelinferno
    Python 3 needed for Invex-Improved
'''

from sys import argv, exit
import requests
from json import decoder
from datetime import timedelta
import os
import platform
import pyperclip

VIEWS = 'Views: '
LENGTH = 'Length: '
PROMPT = '>'
URL = 'https://invidious.osi.kr/'

print('Invex - Invidious URL grabber')

if len(argv) > 1:
    ARGS = ' '.join(argv[1:])
    ISQ = ARGS.replace(' ', '+') # ISQ = input search query
else:
    print('\nInput search query:')
    ISQ = input(PROMPT).replace(' ', '+')

# print search query URL
SQ = URL + 'search?q=' + ISQ # SQ = search query
print(SQ)

# get API
API = URL + 'api/v1/search?q=' + ISQ
try:
    j = requests.get(API).json()
except requests.exceptions.ConnectionError: # no internet
    print('cannot connect to "' + URL + '", please try again later.')
    exit()
except decoder.JSONDecodeError: # invidious api is down
    print('Service is currently unavailable, please try again later.')
    exit()

# declare variables for the search result loop

NUM = [] # reference number to the URL on the printed list
TITLE = [] # title of the reference
k = -1 # reference number
PREFIX = ' ' # to align results evenly

# loop through results
for i in j:
    if k < 9:
        PREFIX = ' '
    else:
        PREFIX = ''
    k += 1
    print(PREFIX + str(k) + ' %s ' % (i['title']) + VIEWS + '%s ' % format(i['viewCount'], 'n') + LENGTH + '%s' % (str(timedelta(seconds=i['lengthSeconds']))))
    # index the URLs and titles to a number that can be called on later
    NUM.append(str(URL + 'watch?v=%s' % (i['videoId'])))
    TITLE.append(str(i['title']))

print('\nPick a number to copy URL and play in MPV:')
PICK = input(PROMPT)
# Macbook
if platform.system() == "Darwin":
    pyperclip.copy(NUM[int(PICK)])
    try:
        os.system(f"mpv {NUM[int(PICK)]}")
    except: exit()
# Windows

# Linux