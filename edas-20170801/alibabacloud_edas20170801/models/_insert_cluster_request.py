# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InsertClusterRequest(DaraModel):
    def __init__(
        self,
        cluster_name: str = None,
        cluster_type: int = None,
        iaas_provider: str = None,
        logical_region_id: str = None,
        network_mode: int = None,
        oversold_factor: int = None,
        vpc_id: str = None,
    ):
        # The name of the cluster.
        # 
        # This parameter is required.
        self.cluster_name = cluster_name
        # The type of the cluster. Valid values:
        # 
        # - 2: ECS cluster.
        # - 3: EDAS built-in Kubernetes cluster.
        # - 5: Kubernetes cluster.
        # 
        # This parameter is required.
        self.cluster_type = cluster_type
        # The IaaS resource provider.
        # 
        # <note>When you select Alibaba Cloud, you must use uppercase Pinyin, such as `ALIYUN`.</note>
        self.iaas_provider = iaas_provider
        # The region ID of the custom namespace. Format: `physical region:custom namespace identifier`, such as `cn-hangzhou:test`.
        self.logical_region_id = logical_region_id
        # The network type. Valid values:
        # 
        # - 1: Classic network.
        # - 2: VPC.
        # 
        # This parameter is required.
        self.network_mode = network_mode
        # **[Deprecated]** The CPU overselling ratio for Docker clusters. Valid values:
        # 
        # - 2: 1:2 ratio.
        # - 4: 1:4 ratio.
        # - 8: 1:8 ratio.
        self.oversold_factor = oversold_factor
        # The ID of the VPC. This parameter is required if the network type is set to VPC.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.iaas_provider is not None:
            result['IaasProvider'] = self.iaas_provider

        if self.logical_region_id is not None:
            result['LogicalRegionId'] = self.logical_region_id

        if self.network_mode is not None:
            result['NetworkMode'] = self.network_mode

        if self.oversold_factor is not None:
            result['OversoldFactor'] = self.oversold_factor

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('IaasProvider') is not None:
            self.iaas_provider = m.get('IaasProvider')

        if m.get('LogicalRegionId') is not None:
            self.logical_region_id = m.get('LogicalRegionId')

        if m.get('NetworkMode') is not None:
            self.network_mode = m.get('NetworkMode')

        if m.get('OversoldFactor') is not None:
            self.oversold_factor = m.get('OversoldFactor')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

