# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAuthorizedAgentsRequest(DaraModel):
    def __init__(
        self,
        permission: str = None,
        target_user_id: int = None,
        tenant_id: str = None,
    ):
        # 权限类型：USE=使用权限, MANAGE=管理权限，默认 USE
        self.permission = permission
        # 目标用户 ID，管理员代查指定用户可用的数字员工时传入（需 APPLICATION_AGENT_VIEW 权限）；不传则查询调用方自身
        self.target_user_id = target_user_id
        # 租户ID，公共参数，缺省时使用调用方默认租户
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.permission is not None:
            result['permission'] = self.permission

        if self.target_user_id is not None:
            result['targetUserId'] = self.target_user_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('permission') is not None:
            self.permission = m.get('permission')

        if m.get('targetUserId') is not None:
            self.target_user_id = m.get('targetUserId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

