# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNetworkAclRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        network_acl_name: str = None,
    ):
        # The description of the network ACL.
        # 
        # The description must be 1 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # Enter a name for the network ACL.
        # 
        # The name must be 1 to 128 characters in length and cannot start with http:// or https://.
        self.network_acl_name = network_acl_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.network_acl_name is not None:
            result['NetworkAclName'] = self.network_acl_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('NetworkAclName') is not None:
            self.network_acl_name = m.get('NetworkAclName')

        return self

