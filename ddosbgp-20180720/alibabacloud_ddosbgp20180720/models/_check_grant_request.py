# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckGrantRequest(DaraModel):
    def __init__(
        self,
        is_slr: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # Specifies whether to allow Anti-DDoS Origin to check the service-linked role. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_slr = is_slr
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_slr is not None:
            result['IsSlr'] = self.is_slr

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSlr') is not None:
            self.is_slr = m.get('IsSlr')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

