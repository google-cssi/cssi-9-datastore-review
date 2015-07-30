import jinja2
import os
import webapp2
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class BlogPostSaver(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('thanks.html')
        self.response.write(template.render())

class BlogPostViewer(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('viewer.html')
        self.response.write(template.render())

class BlogPostCreator(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('creator.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', BlogPostCreator),
    ('/save', BlogPostSaver),
    ('/view', BlogPostViewer)
], debug=True)
