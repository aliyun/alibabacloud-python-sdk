# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDiskReplicaPairProgressRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        replica_pair_id: str = None,
    ):
        # The region ID of the replication pair.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the replication pair. You can call the [DescribeDiskReplicaPairs](https://help.aliyun.com/document_detail/354206.html)operation to query the IDs of existing replication pairs.
        # 
        # This parameter is required.
        self.replica_pair_id = replica_pair_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')

        return self

