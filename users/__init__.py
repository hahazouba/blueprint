# -*- coding:utf-8 -*-

from flask import Blueprint

# 创建蓝图
user_blue = Blueprint('user', __name__)
# 放在这里的原因，是应为在导views之前，user_blue必须存在
from users import views
