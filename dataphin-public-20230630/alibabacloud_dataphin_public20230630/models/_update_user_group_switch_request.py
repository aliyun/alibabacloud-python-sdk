# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserGroupSwitchRequest(DaraModel):
    def __init__(
        self,
        active: bool = None,
        op_tenant_id: int = None,
        user_group_id: str = None,
    ):
        # This parameter is required.
        self.active = active
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

