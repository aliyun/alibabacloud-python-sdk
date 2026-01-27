# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ClearPairDrillRequest(DaraModel):
    def __init__(
        self,
        drill_id: str = None,
        pair_id: str = None,
        region_id: str = None,
    ):
        # The ID of the drill. You can call the [DescribePairDrills](https://help.aliyun.com/document_detail/2584480.html) operation to query the disaster recovery drills that were performed on replication pairs in a specific region.
        # 
        # This parameter is required.
        self.drill_id = drill_id
        # The ID of the replication pair. You can call the [DescribeDiskReplicaPairs](https://help.aliyun.com/document_detail/354206.html) operation to query the most recent list of replication pairs, including replication pair IDs.
        # 
        # This parameter is required.
        self.pair_id = pair_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/354276.html) operation to query the most recent list of regions in which async replication is supported.
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
        if self.drill_id is not None:
            result['DrillId'] = self.drill_id

        if self.pair_id is not None:
            result['PairId'] = self.pair_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DrillId') is not None:
            self.drill_id = m.get('DrillId')

        if m.get('PairId') is not None:
            self.pair_id = m.get('PairId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

