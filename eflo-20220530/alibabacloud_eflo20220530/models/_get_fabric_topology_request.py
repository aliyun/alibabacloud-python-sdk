# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetFabricTopologyRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        lni_ids: List[str] = None,
        node_ids: List[str] = None,
        region_id: str = None,
        vpc_id: str = None,
        vpd_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # Lingjun network interface controller ID List
        self.lni_ids = lni_ids
        # Node ID list
        self.node_ids = node_ids
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # Lingjun CIDR block ID
        self.vpd_id = vpd_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.lni_ids is not None:
            result['LniIds'] = self.lni_ids

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('LniIds') is not None:
            self.lni_ids = m.get('LniIds')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')

        return self

