#Import google sign in
from google.appengine.api import users
from google.appengine.ext import ndb

import webapp2
import jinja2


#Import os for finding jinja
import os
from finance.finance import FinancePage
from finance.checkbook import CheckBook

#Make sure to setup the template rendering evironment in the templates directory
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates/'),
    extensions=['jinja2.ext.autoescape'])

class User(ndb.Model):
	"""User model for the datastore to hold so we can have a single user object to deal with"""
	user_id = ndb.StringProperty() #Store the user_id() because it won't ever change


class LandingPage(webapp2.RequestHandler):

	def get(self):
		user = users.get_current_user()

		if user:
			#Store the user information if they don't exist already 

			template_values = {
				'username': user.user_id(),
			}
			template = JINJA_ENVIRONMENT.get_template('index.html')
			self.response.write(template.render(template_values))
		else:
			self.redirect(users.create_login_url(self.request.uri))

		

application = webapp2.WSGIApplication([
    ('/', LandingPage),

], debug=True)