import pandas as pd
import sys
import tornado.ioloop
import tornado.web
import tornado.concurrent
import json
import os
import uuid
import numpy as np
import time

MAX_PROCESS =1 # 0 --> auto 
MAX_WORKERS = 8 
PORT = 50001

class nxny3Handler(tornado.web.RequestHandler):
  executor = tornado.concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS)

  def post(self, *args, **kwargs):
    global df, money
    val = self.request.arguments['val'][0].decode('utf-8')
    d = df[df["3단계"] == val]
       
    if d.empty:
      d = {'result':'fail', 'si':'', 'gu':'', 'nx':'', 'ny':''}
    else:
      d = d.values[0]
      d = {'result':'ok', 'si':d[2], 'gu':d[3], 'nx':d[5], 'ny':d[6]}

    return self.write(bytes(json.dumps(d), 'UTF-8'))

class nxny2Handler(tornado.web.RequestHandler):
  executor = tornado.concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS)

  def post(self, *args, **kwargs):
    global df, money
    val = self.request.arguments['val'][0].decode('utf-8')
    d = df[df["2단계"] == val]
       
    if d.empty:
      d = {'result':'fail', 'si':'', 'gu':'', 'nx':'', 'ny':''}
    else:
      d = d.values[0]
      d = {'result':'ok', 'si':d[2], 'gu':d[3], 'nx':d[5], 'ny':d[6]}

    return self.write(bytes(json.dumps(d), 'UTF-8'))

def make_app():
  return tornado.web.Application([
    ("/nxny_from_3", nxny3Handler),
    ("/nxny_from_2", nxny2Handler)
  ])

if __name__ == "__main__":
  df = pd.read_excel('nxny_20161004.xlsx')
  app = make_app()
  server = tornado.httpserver.HTTPServer(app)
  server.bind(PORT)
  server.start(MAX_PROCESS) # forks one process per cpu 0
  print('Tornado Server Start !')
  tornado.ioloop.IOLoop.current().start()
