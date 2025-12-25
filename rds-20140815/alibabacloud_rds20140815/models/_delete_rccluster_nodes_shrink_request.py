# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRCClusterNodesShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_ids_shrink: str = None,
        nodes_shrink: str = None,
        region_id: str = None,
        vpc_id: str = None,
    ):
        # The instance IDs.
        self.instance_ids_shrink = instance_ids_shrink
        # The node information.
        self.nodes_shrink = nodes_shrink
        # The region ID.
        self.region_id = region_id
        # The virtual private cloud (VPC) ID.
        # 
        # >  This is a reserved parameter.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink

        if self.nodes_shrink is not None:
            result['Nodes'] = self.nodes_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')

        if m.get('Nodes') is not None:
            self.nodes_shrink = m.get('Nodes')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

