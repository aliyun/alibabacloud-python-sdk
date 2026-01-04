# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeL7RsPolicyRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        real_servers: List[str] = None,
        resource_group_id: str = None,
    ):
        # The domain name of the website to query.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) operation to query the domain names for which forwarding rules are configured.
        # 
        # This parameter is required.
        self.domain = domain
        # An array that consists of N addresses of origin servers to query. The maximum value of N is 200. You can specify up to 200 addresses.
        self.real_servers = real_servers
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](https://help.aliyun.com/document_detail/94485.html).
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.real_servers is not None:
            result['RealServers'] = self.real_servers

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

