# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InsertRoleRequest(DaraModel):
    def __init__(
        self,
        action_data: str = None,
        role_name: str = None,
    ):
        # The set of permissions to be granted to the role. The value is in the format of `Permission group ID 1:Permission serial number 1;...;Permission group ID n:Permission serial number n`. Example: `1:1;1:2;2:1;2:2`. For more information about permission groups and permission serial numbers, see [ListAuthority](https://help.aliyun.com/document_detail/149409.html).
        # 
        # This parameter is required.
        self.action_data = action_data
        # The name of the role.
        # 
        # This parameter is required.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_data is not None:
            result['ActionData'] = self.action_data

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionData') is not None:
            self.action_data = m.get('ActionData')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

