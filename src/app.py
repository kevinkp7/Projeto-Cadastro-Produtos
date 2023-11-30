from flask import Flask
from src.routes.routes import *

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY = '1234')

app.add_url_rule(routes["index_route"], view_func=routes["indexcontroller"])

app.add_url_rule(routes["delete_route"], view_func=routes["delete_controller"])

app.add_url_rule(routes["update_route"], view_func=routes["update_controller"])

app.add_url_rule(routes["categories_route"], view_func=routes["categories_controller"])




