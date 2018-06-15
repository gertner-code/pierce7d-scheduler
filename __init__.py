#!/usr/bin/env python

import os
from flask import (Flask,
                   g,
                   session,
                   render_template,
                   request,
                   redirect,
                   jsonify,
                   url_for,
                   flash)
from requests_oauthlib import OAuth2Session
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Genre, Book, User, Base
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)


if __name__ == '__main__':
    """Run webpage on open."""
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)