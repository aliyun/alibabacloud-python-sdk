# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyGroupPropertyRequest(DaraModel):
    def __init__(
        self,
        data: str = None,
    ):
        # The new property information of the server group after modification. The following parameters are described:
        # 
        # - **groupFlag**: The type of the server group. Valid values: **0** (default group) | **1** (other group).
        # - **groupId**: The ID of the server group.
        # - **groupIndex**: The sorting number of the server group. Sorted in ascending order.
        # - **groupName**: The name of the server group. Set this parameter to the new name of the server group. The new name must be different from the original name.
        # 
        # > Call the [DescribeAllGroups](~~DescribeAllGroups~~) operation to obtain the values of groupFlag and groupId. The values of groupFlag and groupId cannot be modified. Only the value of groupName can be modified.
        # 
        # This parameter is required.
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        return self

