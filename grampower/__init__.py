import os
import json
from flask.app import Flask


app = Flask(__name__)

app.config.from_object('config')

app.url_map.strict_slashes = False

import grampower.controllers