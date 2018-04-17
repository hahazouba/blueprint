from . import goods_blue


@goods_blue.route('/goods_info')
def goods_info():
    return 'goods_info'
