# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeStsGrantStatusRequest(DaraModel):
    def __init__(
        self,
        resource_group_id: str = None,
        role: str = None,
    ):
        # The ID of the resource group to which the Anti-DDoS Proxy instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the default resource group is used.
        self.resource_group_id = resource_group_id
        # The name of the RAM role that you want to query. The value is fixed as **AliyunDDoSCOODefaultRole**, which indicates the default role of Anti-DDoS Proxy.
        # 
        # > Anti-DDoS Proxy use this role by default to access your resources in other cloud services.
        # 
        # This parameter is required.
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

