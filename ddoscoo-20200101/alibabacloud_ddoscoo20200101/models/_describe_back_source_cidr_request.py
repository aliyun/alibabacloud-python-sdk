# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackSourceCidrRequest(DaraModel):
    def __init__(
        self,
        ip_version: str = None,
        line: str = None,
        resource_group_id: str = None,
    ):
        # The IP version of the back-to-origin CIDR blocks.
        # 
        # *   **Ipv4**
        # *   **Ipv6**
        self.ip_version = ip_version
        # The Internet service provider (ISP) line that you want to query.
        self.line = line
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.line is not None:
            result['Line'] = self.line

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Line') is not None:
            self.line = m.get('Line')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

