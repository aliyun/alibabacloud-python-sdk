# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClustersV1Request(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_spec: str = None,
        cluster_type: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        profile: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster specification. This parameter is valid only when `cluster_type` is set to `ManagedKubernetes` and the `profile` parameter is specified. Valid values:
        # 
        # - `ack.standard`: Standard
        # 
        # - `ack.pro.small`: Pro
        # 
        # - `ack.pro.xlarge`: Pro XL
        # 
        # - `ack.pro.2xlarge`: Pro 2XL
        # 
        # - `ack.pro.4xlarge`: Pro 4XL (Contact customer service to enable this option.)
        # 
        # Pro XL, Pro 2XL, and Pro 4XL are three tiers provided by the <props="china">[ACK Pro provisioned control plane](https://help.aliyun.com/ack/ack-managed-and-ack-dedicated/user-guide/ack-pro-provisioned-control-plane)<props="intl">[ACK Pro provisioned control plane](https://www.alibabacloud.com/help/ack/ack-managed-and-ack-dedicated/user-guide/ack-pro-provisioned-control-plane). These tiers pre-allocate and dedicate control plane resources to ensure a consistently high, predictable level of performance for API concurrency and pod scheduling. They are suitable for AI training and inference, ultra-large-scale clusters, and mission-critical workloads.
        # 
        # For information about the cluster management fees for Pro and provisioned control plane editions, see <props="china">[Cluster management fee](https://help.aliyun.com/ack/ack-managed-and-ack-dedicated/product-overview/cluster-management-fee)<props="intl">[Cluster management fee](https://www.alibabacloud.com/help/ack/ack-managed-and-ack-dedicated/product-overview/cluster-management-fee).
        self.cluster_spec = cluster_spec
        # The cluster type.
        # 
        # - `Kubernetes`: an ACK dedicated cluster.
        # 
        # - `ManagedKubernetes`: an ACK managed cluster. This type includes ACK managed clusters (Pro and Standard), ACK Serverless clusters (Pro and Standard), ACK Edge clusters (Pro and Standard), and ACK Lingjun clusters (Pro).
        # 
        # - `ExternalKubernetes`: a registered cluster.
        self.cluster_type = cluster_type
        # The name of the cluster.
        self.name = name
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # When `cluster_type` is set to `ManagedKubernetes`, you can further specify a sub-type of the cluster.
        # 
        # - `Default`: an ACK managed cluster. This includes ACK Pro and ACK Standard clusters.
        # 
        # - `Edge`: an ACK Edge cluster. This includes ACK Edge Pro and ACK Edge Standard clusters.
        # 
        # - `Serverless`: an ACK Serverless cluster. This includes ACK Serverless Pro and ACK Serverless Standard clusters.
        # 
        # - `Lingjun`: an ACK Lingjun cluster (Pro edition).
        self.profile = profile
        # The ID of the region to which the clusters belong.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.cluster_spec is not None:
            result['cluster_spec'] = self.cluster_spec

        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type

        if self.name is not None:
            result['name'] = self.name

        if self.page_number is not None:
            result['page_number'] = self.page_number

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.profile is not None:
            result['profile'] = self.profile

        if self.region_id is not None:
            result['region_id'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('cluster_spec') is not None:
            self.cluster_spec = m.get('cluster_spec')

        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('profile') is not None:
            self.profile = m.get('profile')

        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')

        return self

