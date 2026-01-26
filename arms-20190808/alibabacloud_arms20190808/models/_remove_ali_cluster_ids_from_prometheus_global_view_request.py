# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveAliClusterIdsFromPrometheusGlobalViewRequest(DaraModel):
    def __init__(
        self,
        cluster_ids: str = None,
        global_view_cluster_id: str = None,
        group_name: str = None,
        region_id: str = None,
    ):
        # The IDs of clusters. Separate multiple IDs with commas (,).
        # 
        # This parameter is required.
        self.cluster_ids = cluster_ids
        # The ID of the global aggregation instance.
        # 
        # This parameter is required.
        self.global_view_cluster_id = global_view_cluster_id
        # The name of the global aggregation instance.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The region ID.
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
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids

        if self.global_view_cluster_id is not None:
            result['GlobalViewClusterId'] = self.global_view_cluster_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')

        if m.get('GlobalViewClusterId') is not None:
            self.global_view_cluster_id = m.get('GlobalViewClusterId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

