# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySecurityGroupAttributeRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        security_group_id: str = None,
        security_group_name: str = None,
    ):
        # The description of the security group.
        self.description = description
        # The ID of the security group.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # The name of the security group. The name of a bucket must meet the following requirements:
        # 
        # *   The name must be 2 to 128 characters in length.
        # *   The name must start with a letter but cannot start with http:// or https://.
        # *   The name can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.security_group_name = security_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')

        return self

