# -*- coding:utf-8 -*-


from . import order_blue


@order_blue.route('/order_info')
def order_info():
    return 'order_info'
