# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteGadInstanceRequest(DaraModel):
    def __init__(
        self,
        gad_instance_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the global active database cluster. You can call the GadInstanceName operation to query the cluster ID.
        # 
        # This parameter is required.
        self.gad_instance_name = gad_instance_name
        # The region ID of the central node of the global active database cluster. The central node refers to the primary node. You can call the DescribeGadInstances operation to query the region ID.
        self.region_id = region_id
        # The resource group ID. You can call the DescribeDBInstanceAttribute operation to query the resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gad_instance_name is not None:
            result['GadInstanceName'] = self.gad_instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GadInstanceName') is not None:
            self.gad_instance_name = m.get('GadInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

