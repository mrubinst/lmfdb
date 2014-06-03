# -*- coding: utf-8 -*-
from lmfdb.base import app
from lmfdb.utils import make_logger
from flask import Blueprint

new_object = Blueprint("new_object", __name__, template_folder='templates', static_folder="static")
new_object_logger = make_logger(new_object)


@new_object.context_processor
def body_class():
    return {'body_class': 'new_object'}

#from elliptic_curves import *
import main

app.register_blueprint(new_object, url_prefix="/NewObject")
