# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListRolesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.ListRolesResponseBodyItems] = None,
        message: str = None,
        request_id: str = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 系统内置角色列表（固定 7 个）
        self.items = items
        # 错误描述，成功时为空
        self.message = message
        # 请求追踪 ID
        self.request_id = request_id

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

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListRolesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListRolesResponseBodyItems(DaraModel):
    def __init__(
        self,
        description: str = None,
        role_code: str = None,
        role_name: str = None,
        toggleable: bool = None,
    ):
        # 角色说明（按请求 Accept-Language 国际化）
        self.description = description
        # 角色标识码，用于 createUser/updateUser 的 roleCodes 参数
        self.role_code = role_code
        # 角色显示名称（按请求 Accept-Language 国际化）
        self.role_name = role_name
        # 是否允许启用/停用操作（超级管理员和应用用户不可切换）
        self.toggleable = toggleable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.role_code is not None:
            result['roleCode'] = self.role_code

        if self.role_name is not None:
            result['roleName'] = self.role_name

        if self.toggleable is not None:
            result['toggleable'] = self.toggleable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('roleCode') is not None:
            self.role_code = m.get('roleCode')

        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')

        if m.get('toggleable') is not None:
            self.toggleable = m.get('toggleable')

        return self

