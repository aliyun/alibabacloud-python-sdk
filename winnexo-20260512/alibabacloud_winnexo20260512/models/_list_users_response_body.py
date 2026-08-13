# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListUsersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.ListUsersResponseBodyItems] = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 成员列表
        self.items = items
        # 错误描述，成功时为空
        self.message = message
        # 当前页码
        self.page = page
        # 每页数量
        self.page_size = page_size
        # 请求追踪 ID
        self.request_id = request_id
        # 符合条件的总记录数
        self.total = total

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListUsersResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListUsersResponseBodyItems(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        display_name: str = None,
        gmt_create: str = None,
        is_active: bool = None,
        last_login_time: str = None,
        role_codes: List[str] = None,
        user_id: int = None,
    ):
        # WINNEXO 登录账号
        self.account_id = account_id
        # 用户显示名称
        self.display_name = display_name
        # 加入租户时间
        self.gmt_create = gmt_create
        # 启用/停用状态
        self.is_active = is_active
        # 最后登录时间
        self.last_login_time = last_login_time
        # 用户拥有的系统角色 code 列表
        self.role_codes = role_codes
        # 用户ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.is_active is not None:
            result['isActive'] = self.is_active

        if self.last_login_time is not None:
            result['lastLoginTime'] = self.last_login_time

        if self.role_codes is not None:
            result['roleCodes'] = self.role_codes

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('isActive') is not None:
            self.is_active = m.get('isActive')

        if m.get('lastLoginTime') is not None:
            self.last_login_time = m.get('lastLoginTime')

        if m.get('roleCodes') is not None:
            self.role_codes = m.get('roleCodes')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

