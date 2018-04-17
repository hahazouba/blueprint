# -*- coding:utf-8 -*-

from flask import Flask
from users import user_blue
from order import order_blue
from goods import goods_blue

app = Flask(__name__)
# 讲蓝图注册到app，让知道那个路由跟蓝图建立关联
app.register_blueprint(user_blue)
app.register_blueprint(order_blue)
app.register_blueprint(goods_blue)


@app.route('/')
def index():
    return 'index'


# # 被拷贝到user
# @app.route('/user')
# def user_info():
#     return 'user_info'


# @app.route('/order')
# def order_info():
#     return 'order_info'


if __name__ == '__main__':
    print app.url_map
    app.run(debug=True)
