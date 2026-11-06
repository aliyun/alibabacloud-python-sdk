# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListCollaborationGroupMembersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.ListCollaborationGroupMembersResponseBodyItems] = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # 公共业务状态码，由后端Code字段映射；错误时用于识别失败原因。
        self.code = code
        # 当前页记录列表；没有匹配记录时返回空数组。
        self.items = items
        # 公共错误说明，由后端Message字段映射；错误时描述失败原因。
        self.message = message
        # 当前返回页的页码，从1开始。
        self.page = page
        # 当前分页设置的每页记录数。
        self.page_size = page_size
        # 请求追踪ID，由后端RequestId字段映射，用于排查调用失败。
        self.request_id = request_id
        # 满足查询条件的记录总数，不是当前页记录数。
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
                temp_model = main_models.ListCollaborationGroupMembersResponseBodyItems()
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

class ListCollaborationGroupMembersResponseBodyItems(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        is_active: bool = None,
        role: str = None,
        user_id: str = None,
    ):
        # 成员显示名称；未设置时为空。
        self.display_name = display_name
        # 租户账号是否启用。本接口只返回有效且账号启用的成员，值为true；不代表HR在职状态。
        self.is_active = is_active
        # 成员在空间内的角色：ADMIN为管理员，MEMBER为普通成员。
        self.role = role
        # 平台用户ID，字符串形式，可用作转交待办的目标用户ID。
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.is_active is not None:
            result['isActive'] = self.is_active

        if self.role is not None:
            result['role'] = self.role

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('isActive') is not None:
            self.is_active = m.get('isActive')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

