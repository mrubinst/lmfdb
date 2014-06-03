# -*- coding: utf-8 -*-
# new_object.py

import re

from lmfdb.base import app, r
import flask
from flask import Flask, session, g, render_template, url_for, make_response, request, redirect
from sage.all import *
import tempfile
import os
from pymongo import ASCENDING
from lmfdb.utils import to_dict, parse_range, make_logger, url_character
from lmfdb.new_object import new_object, new_object_logger

###############################################################################
#   Route functions
#   Do not use url_for on these, use url_character defined in lmfdb.utils
###############################################################################

@new_object.route("/")
def new_object_front_page():

    args = to_dict(request.args)
    info = {}
    info['bread'] = [ ('NewObject','/NewObject') ]

    info['title'] = 'New Object Page'
    info['something_generated'] = 1+1

    return render_template("new_object_front.html", **info)

@new_object.route("/<label>")
def new_object_page(label=None):

    args = to_dict(request.args)
    info = {}
    info['bread'] = [ ('NewObject','/NewObject') ]

    info['title'] = 'New Object %s' %label
    info['name'] = label
    info['something_generated'] = label
    info['properties2'] = [('name',label),('favourite colour','green')]

    return render_template("new_object.html", **info)

