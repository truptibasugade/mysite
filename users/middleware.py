from datetime import datetime, timedelta
from django.conf import settings
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from users import views
from users import urls

class AutoLogout:
  def process_request(self, request):
    # if not request.user.is_authenticated() :
      
    #   return HttpResponseRedirect('/users/')

    try:
      if datetime.now() - request.session['last_touch'] > timedelta( 0, settings.AUTO_LOGOUT_DELAY , 0):
        auth.logout(request)
        del request.session['last_touch']
        return 
    except KeyError:
      pass

    request.session['last_touch'] = datetime.now()