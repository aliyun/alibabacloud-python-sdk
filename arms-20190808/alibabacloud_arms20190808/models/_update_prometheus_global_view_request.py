# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePrometheusGlobalViewRequest(DaraModel):
    def __init__(
        self,
        all_sub_clusters_success: bool = None,
        cluster_id: str = None,
        group_name: str = None,
        most_region_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        sub_clusters_json: str = None,
    ):
        # To edit a GlobalView aggregated instance, do you require all passed child instances to be verified successfully before creating a GlobalView instance (optional, default to false):
        # - true
        # - false
        self.all_sub_clusters_success = all_sub_clusters_success
        # The ID of the Prometheus instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The name of the global aggregation instance.
        self.group_name = group_name
        # The region ID of the global aggregation instance.
        self.most_region_id = most_region_id
        # The ID of the region in which the Prometheus instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the Prometheus instance belongs.
        self.resource_group_id = resource_group_id
        # The data sources of the Prometheus instance for GlobalView.
        # 
        # This parameter is required.
        self.sub_clusters_json = sub_clusters_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_sub_clusters_success is not None:
            result['AllSubClustersSuccess'] = self.all_sub_clusters_success

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.most_region_id is not None:
            result['MostRegionId'] = self.most_region_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sub_clusters_json is not None:
            result['SubClustersJson'] = self.sub_clusters_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllSubClustersSuccess') is not None:
            self.all_sub_clusters_success = m.get('AllSubClustersSuccess')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('MostRegionId') is not None:
            self.most_region_id = m.get('MostRegionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SubClustersJson') is not None:
            self.sub_clusters_json = m.get('SubClustersJson')

        return self

