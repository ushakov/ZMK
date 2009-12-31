#!/usr/bin/python

import urllib
import string

import wsgiref.handlers
from google.appengine.ext import webapp

import template
import json

class HomeHandler(webapp.RequestHandler):
  def get(self):
    tpl = {}
    self.response.out.write(template.Render("index.html", tpl))

def getp(d, k):
  if k in d:
    return d[k]
  return ""

class KartHandler(webapp.RequestHandler):
  def get(self):
    tpl = {}
    params = dict(self.request.params)

    name = getp(params, 'name')
    klass = getp(params,'class')
    school = getp(params,'school')
    index = getp(params,'index')
    address = getp(params,'address')
    phone = getp(params,'phone')

    d = {
      'n': name.encode("utf8"),
      'c': klass.encode("utf8"),
      's': school.encode("utf8"),
      'i': index.encode("utf8"),
      'a': address.encode("utf8"),
      'p': phone.encode("utf8")}
    content = json.write(d)
    image_url = ("http://chart.apis.google.com/chart?" + 
                 urllib.urlencode({'cht': 'qr',
                                   'chs': '250x250',
                                   'chl': content}))
    d['image_url'] = image_url

    self.response.out.write(template.Render('kart.html', d))

urlmap = [('/', HomeHandler),
          ('/card', KartHandler)]

def main():
  application = webapp.WSGIApplication(urlmap,
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
