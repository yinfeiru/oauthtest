from __future__ import unicode_literals

from django.utils.safestring import mark_safe
from django.shortcuts import render as django_render
from django.http import HttpResponse

from requests_oauthlib import OAuth2Session

import requests

import logging
import sys
log = logging.getLogger('oauthlib')
log.addHandler(logging.StreamHandler(sys.stdout))
log.setLevel(logging.DEBUG)


client_secret = ''
client_id = ''

def index(request):
    return django_render(
        request,
        'index.html'
    )

def authenticate(request):
    oauth_session = OAuth2Session(
        client_id=client_id,
        redirect_uri='https://yinfei.dev.mixpanel.org/oauthtest/authorization_code/oauth_credentials', # the callback which fetches the access token
                      
    )
    auth_url, state = oauth_session.authorization_url(
        url='https://mixpanel.com/oauth/authorize/',  # eg. https://www.example.com/oauth/authorize
    )
    request.session['oauth_state'] = state
    return django_render(request, 'redirect_page.html', {'redirect_url': mark_safe(auth_url)})

def oauth_credentials(request):
    oauth_session = OAuth2Session(
        client_id=client_id,
        redirect_uri='https://yinfei.dev.mixpanel.org/oauthtest/authorization_code/oauth_credentials', # the callback which fetches the access token
    )
    authorization_response = 'https://yinfei.dev.mixpanel.org/' + request.get_full_path() # eg. https://www.example.com
    token = oauth_session.fetch_token(
        token_url='https://mixpanel.com/oauth/token/', # eg. https://www.example.com/oauth/token
        client_secret=client_secret,
        authorization_response=authorization_response,
    )
    import pdb;pdb.set_trace()
    auth_header = {'Authorization': 'Bearer ' + token['access_token'].encode('utf-8')}
    response = requests.get('https://yinfei.dev.mixpanel.org/api/2.0/engage/?project_id=3', headers=auth_header)
# requests.get('https://stage04.mixpanel.com/api/2.0/funnels/?funnel_id=714349&from_date=2017-08-16&to_date=2017-09-15&limit=200&unit=day', headers={'Authorization': 'Bearer '})
    request.session['oauth_token'] = token
    return django_render(
        request,
        'index.html'
    )

def refresh_token(request):
    oauth_session = OAuth2Session(
        client_id=client_id,
        token = request.session.pop('oauth_token'),
    )
    token = oauth_session.refresh_token(
        token_url='https://www.mixpanel.com/oauth/token/',
        client_secret=client_secret,
        client_id=client_id,
    )

def test_webhook(request):
    print 1
    return HttpResponse(status=200)
