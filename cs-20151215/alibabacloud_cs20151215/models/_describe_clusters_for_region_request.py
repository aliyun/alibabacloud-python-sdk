# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClustersForRegionRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_spec: str = None,
        cluster_type: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        profile: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # Queries clusters of a specified specification. Valid values:
        # 
        # - `ack.standard`: Basic
        # - `ack.pro.small`: Pro
        # - `ack.pro.xlarge`: Pro XL
        # - `ack.pro.2xlarge`: Pro 2XL
        # - `ack.pro.4xlarge`: Pro 4XL (contact customer service to add your account to the whitelist)
        # 
        # Pro XL, Pro 2XL, and Pro 4XL are three tiers provided by <props="china">[ACK Pro Provisioned Control Plane](https://help.aliyun.com/ack/ack-managed-and-ack-dedicated/user-guide/ack-pro-provisioned-control-plane)<props="intl">[ACK Pro Provisioned Control Plane](https://www.alibabacloud.com/help/ack/ack-managed-and-ack-dedicated/user-guide/ack-pro-provisioned-control-plane). By pre-allocating and dedicating control plane resources, these tiers ensure that API concurrency and Pod scheduling capabilities remain at a consistently high level. They are suitable for AI training and inference, ultra-large-scale clusters, and mission-critical workloads.
        # 
        # For information about cluster management fees for Pro and Provisioned Control Plane editions, see <props="china">[Cluster management fees](https://help.aliyun.com/ack/ack-managed-and-ack-dedicated/product-overview/cluster-management-fee)<props="intl">[Cluster management fees](https://www.alibabacloud.com/help/ack/ack-managed-and-ack-dedicated/product-overview/cluster-management-fee).
        self.cluster_spec = cluster_spec
        # Queries clusters of a specified type. Valid values:
        # - Kubernetes: ACK dedicated cluster.
        # - ManagedKubernetes: ACK managed cluster types, including ACK managed clusters (ACK Pro and ACK Basic), ACK Serverless clusters (Pro and Basic), ACK Edge clusters (Pro and Basic), and ACK Lingjun clusters (Pro).
        # - ExternalKubernetes: registered cluster.
        self.cluster_type = cluster_type
        # Fuzzy search by cluster name.
        self.name = name
        # The page number.
        self.page_number = page_number
        # The number of records per page.
        self.page_size = page_size
        # Queries clusters of a specified subtype. Valid values:
        # - Default: ACK managed cluster, including ACK Pro and ACK Basic.
        # - Edge: ACK Edge cluster, including ACK Edge Pro and ACK Edge Basic.
        # - Serverless: ACK Serverless cluster, including ACK Serverless Pro and ACK Serverless Basic.
        # - LingJun: ACK Lingjun cluster, available in Pro.
        self.profile = profile

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

        return self

