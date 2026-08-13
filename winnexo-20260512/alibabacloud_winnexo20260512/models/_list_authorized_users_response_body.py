# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListAuthorizedUsersResponseBody(DaraModel):
    def __init__(
        self,
        auth_mode: str = None,
        code: str = None,
        items: List[main_models.ListAuthorizedUsersResponseBodyItems] = None,
        message: str = None,
        request_id: str = None,
        total: int = None,
    ):
        # 授权模式：SPECIFIED_USERS / ALL_USERS
        self.auth_mode = auth_mode
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 已授权对象列表
        self.items = items
        # 错误描述，成功时为空
        self.message = message
        # 请求追踪 ID
        self.request_id = request_id
        # 授权记录总数
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
        if self.auth_mode is not None:
            result['authMode'] = self.auth_mode

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

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authMode') is not None:
            self.auth_mode = m.get('authMode')

        if m.get('code') is not None:
            self.code = m.get('code')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListAuthorizedUsersResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListAuthorizedUsersResponseBodyItems(DaraModel):
    def __init__(
        self,
        expire_date: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        granted_by: int = None,
        grantee_id: str = None,
        grantee_type: str = None,
        id: int = None,
        member_count: int = None,
        permissions: List[str] = None,
        user_group_id: str = None,
        user_group_name: str = None,
        user_id: int = None,
        user_name: str = None,
    ):
        # 授权截止时间戳（毫秒）
        self.expire_date = expire_date
        # 创建时间
        self.gmt_create = gmt_create
        # 最后修改时间
        self.gmt_modified = gmt_modified
        # 授权人用户 ID
        self.granted_by = granted_by
        # 被授权对象 ID
        self.grantee_id = grantee_id
        # 被授权对象类型：USER / USER_GROUP
        self.grantee_type = grantee_type
        # 授权记录 ID
        self.id = id
        # 用户组成员数
        self.member_count = member_count
        # 已授权的权限列表
        self.permissions = permissions
        # 用户组 ID（granteeType=USER_GROUP 时有值）
        self.user_group_id = user_group_id
        # 用户组名
        self.user_group_name = user_group_name
        # 用户 ID（granteeType=USER 时有值）
        self.user_id = user_id
        # 用户名
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_date is not None:
            result['expireDate'] = self.expire_date

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.granted_by is not None:
            result['grantedBy'] = self.granted_by

        if self.grantee_id is not None:
            result['granteeId'] = self.grantee_id

        if self.grantee_type is not None:
            result['granteeType'] = self.grantee_type

        if self.id is not None:
            result['id'] = self.id

        if self.member_count is not None:
            result['memberCount'] = self.member_count

        if self.permissions is not None:
            result['permissions'] = self.permissions

        if self.user_group_id is not None:
            result['userGroupId'] = self.user_group_id

        if self.user_group_name is not None:
            result['userGroupName'] = self.user_group_name

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.user_name is not None:
            result['userName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expireDate') is not None:
            self.expire_date = m.get('expireDate')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('grantedBy') is not None:
            self.granted_by = m.get('grantedBy')

        if m.get('granteeId') is not None:
            self.grantee_id = m.get('granteeId')

        if m.get('granteeType') is not None:
            self.grantee_type = m.get('granteeType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('memberCount') is not None:
            self.member_count = m.get('memberCount')

        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')

        if m.get('userGroupId') is not None:
            self.user_group_id = m.get('userGroupId')

        if m.get('userGroupName') is not None:
            self.user_group_name = m.get('userGroupName')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

