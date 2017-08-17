from __future__ import unicode_literals

from django.utils.safestring import mark_safe
from django.shortcuts import render as django_render

from requests_oauthlib import OAuth2Session

import requests

import logging
import sys
log = logging.getLogger('oauthlib')
log.addHandler(logging.StreamHandler(sys.stdout))
log.setLevel(logging.DEBUG)


client_secret = 'YOUR_CLIENT_SECRET'
client_id = 'YOUR_CLIENT_ID'

def index(request):
    return django_render(
        request,
        'index.html'
    )

def authenticate(request):
    oauth_session = OAuth2Session(
        client_id=client_id,
        redirect_uri='CALLBACK', # the callback which fetches the access token
    )
    auth_url, state = oauth_session.authorization_url(
        url='OAUTH_SERVER',  # eg. https://www.example.com/oauth/authorize
    )
    request.session['oauth_state'] = state
    return django_render(request, 'redirect_page.html', {'redirect_url': mark_safe(auth_url)})

def oauth_credentials(request):
    oauth_session = OAuth2Session(
        client_id=client_id,
        redirect_uri='CALLBACK', # same as the CALLBACK above
        state=request.session.pop('oauth_state'),
    )
    authorization_response = 'YOUR_SERVER' + request.get_full_path() # eg. https://www.example.com
    token = oauth_session.fetch_token(
        token_url='ACCESS_TOKEN_API', # eg. https://www.example.com/oauth/token
        client_secret=client_secret,
        authorization_response=authorization_response,
    )


