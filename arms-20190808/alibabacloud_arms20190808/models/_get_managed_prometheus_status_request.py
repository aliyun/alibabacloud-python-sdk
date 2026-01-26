# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetManagedPrometheusStatusRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        vpc_id: str = None,
    ):
        # The cluster ID. This parameter is required if the ClusterType parameter is set to ask.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The type of the cluster. Valid values: ask and ecs.
        # 
        # This parameter is required.
        self.cluster_type = cluster_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group id of the Prometheus instance.
        self.resource_group_id = resource_group_id
        # The ID of the virtual private cloud (VPC). This parameter is required if the ClusterType parameter is set to ecs.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

