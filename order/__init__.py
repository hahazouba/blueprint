from flask import Blueprint

order_blue = Blueprint('order', __name__)
from order import views
