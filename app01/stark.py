# -*- encoding: utf-8 -*-
"""
@File    : stark_simon.py
@Time    : 2022/1/16 20:09
@Author  : simon
@Email   : 294168604@qq.com
@Software: PyCharm
"""

from stark.service.v1 import site, StarkHandler, get_choice_text, StarkModelForm, Option
from app01 import models


# http://127.0.0.1:8000/stark/app01/depart/list/
class DepartHandler(StarkHandler):
    list_display = ['id', 'title', StarkHandler.display_edit, StarkHandler.display_del]

    def save(self, form, is_update=False):
        form.instance.depart_id = 1
        form.save()


# http://127.0.0.1:8000/stark/app01/userinfo/list/
site.register(models.Depart, DepartHandler)


class UserInfoModelForm(StarkModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name', 'gender', 'classes', 'age', 'email']


class UserInfoHandler(StarkHandler):
    # 定制页面显示的列
    list_display = [StarkHandler.display_checkbox,
                    'name',
                    get_choice_text('性别', 'gender'),
                    get_choice_text('班级', 'classes'),
                    'age', 'email', 'depart',
                    StarkHandler.display_edit, StarkHandler.display_del]

    # per_page_count = 1
    has_add_btn = True

    order_list = ['id']
    # 姓名中含有关键字或邮箱中含有关键字
    search_list = ['name__contains', 'email__contains']
    # 定制批量操作功能
    action_list = [StarkHandler.action_multi_delete, ]

    search_group = [Option('gender', is_multi=True),Option('depart', db_condition={'id__gt': 0})
        # MyOption('depart', {'id__gt': 2}),
        # Option('gender', text_func=lambda field_object: field_object[1] + '666'),
    ]

    model_form_class = UserInfoModelForm

    def save(self, form, is_update=False):
        form.instance.depart_id = 1
        form.save()

    # def get_list_display(self):
    #     """
    #     自定义扩展，例如：根据用户的不同显示不同的列
    #     :return:
    #     """
    #     return ['name', 'age']


site.register(models.UserInfo, UserInfoHandler)
