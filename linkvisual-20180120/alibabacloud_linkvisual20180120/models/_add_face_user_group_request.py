# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddFaceUserGroupRequest(DaraModel):
    def __init__(
        self,
        isolation_id: str = None,
        user_group_name: str = None,
    ):
        # The business isolation ID. It is used to isolate data between different business applications under the same Alibaba Cloud account. It supports uppercase and lowercase English letters and digits.
        # 
        # For example, if you have facial recognition businesses in Region A and Region B, you can set different business isolation IDs to distinguish the facial recognition businesses in Region A and Region B.
        # 
        # >Notice: 
        # Save the business isolation ID properly for use when you call other API operations in this business isolation zone.
        # 
        # This parameter is required.
        self.isolation_id = isolation_id
        # The name of the user group. Specify a custom value. The value can be up to 128 characters in length.
        # 
        # This parameter is required.
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id

        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')

        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')

        return self

