#!/usr/bin/python

import wsgiref.handlers
from google.appengine.ext import webapp

import template
import add
import manage
import upload
import export

urlmap = [('/', HomeHandler),
          ('/kart', KartHandler)]

class HomeHandler(webapp.RequestHandler):
  def get(self):
    

def main():
  application = webapp.WSGIApplication(urlmap,
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
