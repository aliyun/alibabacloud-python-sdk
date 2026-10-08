# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListClusterRequest(DaraModel):
    def __init__(
        self,
        logical_region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the namespace. You can call the ListUserDefineRegion operation to query the namespace ID. For more information, see [ListUserDefineRegion](https://help.aliyun.com/document_detail/149377.html).
        # 
        # - If this parameter is left empty, the clusters in the default namespace are queried.
        # 
        # - If this parameter is specified, the clusters in the specified namespace are queried.
        self.logical_region_id = logical_region_id
        # The ID of the resource group. You can call the ListResourceGroup operation to query the resource group ID. For more information, see [ListResourceGroup](https://help.aliyun.com/document_detail/62055.html).
        # 
        # - If this parameter is left empty, the clusters in the default resource group are queried.
        # 
        # - If this parameter is specified, the clusters in the specified resource group are queried.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logical_region_id is not None:
            result['LogicalRegionId'] = self.logical_region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicalRegionId') is not None:
            self.logical_region_id = m.get('LogicalRegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

