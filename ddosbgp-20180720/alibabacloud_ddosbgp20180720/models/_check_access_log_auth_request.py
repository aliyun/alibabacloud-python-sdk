# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckAccessLogAuthRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # For more information about the valid values of this parameter, see [Regions and zones](https://help.aliyun.com/document_detail/188196.html).
        self.region_id = region_id
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management. This parameter is empty by default, which indicates that the Anti-DDoS Origin instance belongs to the default resource group.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

