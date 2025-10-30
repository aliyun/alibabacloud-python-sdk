# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDataShareInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_list_shrink: str = None,
        operation_type: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # The ID of the AnalyticDB for PostgreSQL instance in Serverless mode.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        # 
        # This parameter is required.
        self.instance_list_shrink = instance_list_shrink
        # Specifies whether to enable or disable data sharing. Valid values:
        # 
        # *   **add**: enables data sharing.
        # *   **remove**: disables data sharing.
        # 
        # This parameter is required.
        self.operation_type = operation_type
        self.owner_id = owner_id
        # The ID of the region.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_list_shrink is not None:
            result['InstanceList'] = self.instance_list_shrink

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceList') is not None:
            self.instance_list_shrink = m.get('InstanceList')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

