# -*- encoding: utf-8 -*-
"""
@File    : stark_simon.py
@Time    : 2022/1/16 20:10
@Author  : simon
@Email   : 294168604@qq.com
@Software: PyCharm
"""



from django.shortcuts import HttpResponse
from stark.service.v1 import site, StarkHandler
from app02 import models


class HostHandler(StarkHandler):
    pass


site.register(models.Host, HostHandler)

site.register(models.Role)

site.register(models.Project)
site.register(models.Project, prev='private')