#import the myApp variable from the app package
from app import myApp, myDB
from app.models import User, Video

@myApp.shell_context_processor
def make_shell_context():
	return {'myDB': myDB, 'User': User, 'Video': Video}
