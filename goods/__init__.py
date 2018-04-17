from flask import Blueprint

goods_blue = Blueprint('goods', __name__)

from goods import views
