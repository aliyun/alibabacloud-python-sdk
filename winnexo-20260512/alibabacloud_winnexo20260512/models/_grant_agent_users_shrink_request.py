# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrantAgentUsersShrinkRequest(DaraModel):
    def __init__(
        self,
        expire_date: int = None,
        operating_object_name: str = None,
        permissions_shrink: str = None,
        tenant_id: str = None,
        user_group_ids_shrink: str = None,
        user_ids_shrink: str = None,
    ):
        # 授权截止时间戳（毫秒），不传表示永不过期
        self.expire_date = expire_date
        # 数字员工名称
        # 
        # This parameter is required.
        self.operating_object_name = operating_object_name
        # 权限列表：USE（使用权限）和/或 MANAGE（管理权限），不传时默认仅 USE；不得为空列表
        self.permissions_shrink = permissions_shrink
        # 租户ID，公共参数，缺省时使用调用方默认租户
        self.tenant_id = tenant_id
        # 被授权的用户组 ID 列表（16位 hex 字符串）
        self.user_group_ids_shrink = user_group_ids_shrink
        # 被授权的用户 ID 列表
        self.user_ids_shrink = user_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_date is not None:
            result['expireDate'] = self.expire_date

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.permissions_shrink is not None:
            result['permissions'] = self.permissions_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.user_group_ids_shrink is not None:
            result['userGroupIds'] = self.user_group_ids_shrink

        if self.user_ids_shrink is not None:
            result['userIds'] = self.user_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expireDate') is not None:
            self.expire_date = m.get('expireDate')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('permissions') is not None:
            self.permissions_shrink = m.get('permissions')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('userGroupIds') is not None:
            self.user_group_ids_shrink = m.get('userGroupIds')

        if m.get('userIds') is not None:
            self.user_ids_shrink = m.get('userIds')

        return self

