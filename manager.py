# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import Flask

admin = Blueprint('admin', __name__)
admin.register_blueprint(admin, url_prefix='/admin')


@admin.route('/')
def index():
    return 'admin_index'


if __name__ == '__main__':
    admin.run()
