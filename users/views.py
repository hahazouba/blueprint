# -*- coding:utf-8 -*-


from . import user_blue


@user_blue.route('/user')
def user_info():
    return 'user_info'


@user_blue.route('/user_list')
def user_list():
    print "user_list"
