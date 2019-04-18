# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import requests
import time,datetime,json

def demo():
  if len(sys.argv) is not 4:
    print("python3 client.py PORT_NUMBER (2|3) VALUE")
    print("2: VALUE(city level name), 3: VALUE(Address1)")
    print(" ex> python3 server.py 50001 2 강북구")
    print("     python3 server.py 50001 3 수유제3동")
    return

  port = sys.argv[1]
  msg_type = 'nxny_from_{}'.format(sys.argv[2]) 
  val = sys.argv[3]

  url = 'http://localhost:{}/{}'.format(port, msg_type)
  try:
    r = requests.post(url, data={'val':val}, timeout=5)
    print("{}: {}".format(str(datetime.datetime.now()), json.loads(r.text)))
  except:
    print("{}: except".format(str(datetime.datetime.now())))
    pass

if __name__ == "__main__":
  demo()
