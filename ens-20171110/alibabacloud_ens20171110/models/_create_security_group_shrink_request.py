# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSecurityGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        permissions_shrink: str = None,
        security_group_name: str = None,
    ):
        # The description. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https://.
        self.description = description
        # An array of security group rules. You can specify up to 200 IDs of security group rules.
        self.permissions_shrink = permissions_shrink
        # The name of the security group. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). It must start with a letter but cannot start with http:// or https://. It can contain letters, digits, colons (:), underscores (_), and hyphens (-). By default, this parameter is empty.
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

        if self.permissions_shrink is not None:
            result['Permissions'] = self.permissions_shrink

        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Permissions') is not None:
            self.permissions_shrink = m.get('Permissions')

        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')

        return self

