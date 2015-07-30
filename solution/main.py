import jinja2
import os
import webapp2
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# Define a BlogPost model for the Datastore
class BlogPost(ndb.Model):
    db_title = ndb.StringProperty(required=True)
    db_entry = ndb.StringProperty(required=True)

class BlogPostSaver(webapp2.RequestHandler):
    def post(self):
        # Get the title and entry values from the form request.
        title = self.request.get('title_in_request')
        entry = self.request.get('entry_in_request')
        # Create a new BlogPost with these values.
        db_blog_post = BlogPost(db_title=title, db_entry=entry)
        # Save it in the database.
        db_blog_post.put()
        # Render the thank you page. (No template parameters needed.)
        template = JINJA_ENVIRONMENT.get_template('thanks.html')
        self.response.write(template.render())

class BlogPostViewer(webapp2.RequestHandler):
    def get(self):
        # Query all entries from the BlogPost table.
        blog_query = BlogPost.query()
        # |blog_data| now contains a list of BlogPost objects.
        blog_data = blog_query.fetch()
        template = JINJA_ENVIRONMENT.get_template('viewer.html')
        # Send |blog_data| to viewer.html as the value of 'entries'.
        self.response.write(template.render({'entries' : blog_data}))

class BlogPostCreator(webapp2.RequestHandler):
    def get(self):
        # Render the creator page. (No template parameters needed.)
        template = JINJA_ENVIRONMENT.get_template('creator.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', BlogPostCreator),
    ('/save', BlogPostSaver),
    ('/view', BlogPostViewer)
], debug=True)
