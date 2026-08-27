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
        # The userId of the responsible user.
        self.permission = permission
        # The target user ID.
        self.target_user_id = target_user_id
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
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

