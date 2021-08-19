#! python3
# mclip.py - A multi-clipboard program.

text = {'agree': """yes, I agree. That sounds fine to me.""",
       'busy': """Sorry, can we do this later this week or next week?""",
       'upsell': """Would you consider making this a monthly donation?"""}

import pyperclip
import sys
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]    # first command line arg is the keyphrase

if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)
