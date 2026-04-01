# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGadInstancesRequest(DaraModel):
    def __init__(
        self,
        gad_instance_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the global active database cluster.
        # 
        # *   If you leave this parameter empty, this operation returns the details about all global active database clusters that are created within your Alibaba Cloud account.
        # *   If you specify this parameter, this operation returns the details about the global active database cluster that you specify.
        # 
        # >  If you do not specify this parameter when you call this operation for the first time, the IDs of all clusters that are created by using the current account are returned. Then, you can specify the cluster ID to view the cluster details.
        self.gad_instance_name = gad_instance_name
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group.
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

