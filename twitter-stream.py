import sys, time
from pattern.web import Twitter

s = Twitter().stream('#joy, #happiness, #hopeful, #pleasure, #harmony, #kindness, #affection, #love')
for i in range(250):
    time.sleep(1)
    s.update(bytes=1024)
    print s[-1].text if s else ''
