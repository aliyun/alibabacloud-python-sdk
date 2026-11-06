# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListCollaborationGroupsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.ListCollaborationGroupsResponseBodyItems] = None,
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
        # 满足查询条件的有效空间总数，不是当前页记录数。
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
                temp_model = main_models.ListCollaborationGroupsResponseBodyItems()
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

class ListCollaborationGroupsResponseBodyItems(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        current_user_role: str = None,
        name: str = None,
        status: str = None,
    ):
        # 协作空间ID，可用于查询空间成员、查询节点详情及预览对话文件。
        self.collaboration_group_id = collaboration_group_id
        # 当前调用用户在空间内的角色：ADMIN为管理员，MEMBER为普通成员。
        self.current_user_role = current_user_role
        # 协作空间显示名称。
        self.name = name
        # 协作空间状态，当前接口只返回ACTIVE。
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.current_user_role is not None:
            result['currentUserRole'] = self.current_user_role

        if self.name is not None:
            result['name'] = self.name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('currentUserRole') is not None:
            self.current_user_role = m.get('currentUserRole')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

