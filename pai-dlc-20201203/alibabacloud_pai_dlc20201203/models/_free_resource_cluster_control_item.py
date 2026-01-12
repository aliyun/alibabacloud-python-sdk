# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FreeResourceClusterControlItem(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        cross_clusters: bool = None,
        enable_free_resource: bool = None,
        free_resource_cluster_control_id: str = None,
        gmt_create_time: str = None,
        gmt_modify_time: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cross_clusters = cross_clusters
        self.enable_free_resource = enable_free_resource
        self.free_resource_cluster_control_id = free_resource_cluster_control_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modify_time = gmt_modify_time
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterID'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cross_clusters is not None:
            result['CrossClusters'] = self.cross_clusters

        if self.enable_free_resource is not None:
            result['EnableFreeResource'] = self.enable_free_resource

        if self.free_resource_cluster_control_id is not None:
            result['FreeResourceClusterControlId'] = self.free_resource_cluster_control_id

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time

        if self.region_id is not None:
            result['RegionID'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterID') is not None:
            self.cluster_id = m.get('ClusterID')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CrossClusters') is not None:
            self.cross_clusters = m.get('CrossClusters')

        if m.get('EnableFreeResource') is not None:
            self.enable_free_resource = m.get('EnableFreeResource')

        if m.get('FreeResourceClusterControlId') is not None:
            self.free_resource_cluster_control_id = m.get('FreeResourceClusterControlId')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')

        if m.get('RegionID') is not None:
            self.region_id = m.get('RegionID')

        return self

