# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSecurityGroupPermissionsShrinkRequest(DaraModel):
    def __init__(
        self,
        permissions_shrink: str = None,
        security_group_id: str = None,
    ):
        # The security group rules.
        # 
        # This parameter is required.
        self.permissions_shrink = permissions_shrink
        # The ID of the security group.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.permissions_shrink is not None:
            result['Permissions'] = self.permissions_shrink

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Permissions') is not None:
            self.permissions_shrink = m.get('Permissions')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        return self

