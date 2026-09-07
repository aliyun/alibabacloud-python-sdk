# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SyncRecordingRulesRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
        target_clusters: str = None,
    ):
        # The ID of the source cluster whose rules are to be synchronized.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The region ID. This can be the same as the region ID of the source cluster.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of the target clusters for batch synchronization.
        # 
        # This parameter is required.
        self.target_clusters = target_clusters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.target_clusters is not None:
            result['TargetClusters'] = self.target_clusters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TargetClusters') is not None:
            self.target_clusters = m.get('TargetClusters')

        return self

