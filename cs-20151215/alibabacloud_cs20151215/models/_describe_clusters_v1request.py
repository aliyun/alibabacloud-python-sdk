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
        # The cluster specification. This parameter is valid when cluster_type is set to ManagedKubernetes and profile is configured. Valid values:
        # 
        # - ack.standard: Basic Edition.
        # - ack.pro.small: Pro Edition.
        # - ack.pro.xlarge: Pro XL.
        # - ack.pro.2xlarge: Pro 2XL.
        # - ack.pro.4xlarge: Pro 4XL. To use this specification, contact customer service to apply for whitelist access.
        # 
        # Pro XL, Pro 2XL, and Pro 4XL are the three tiers provided by the <props="china">[ACK Pro provisioned control plane](https://help.aliyun.com/ack/ack-managed-and-ack-dedicated/user-guide/ack-pro-provisioned-control-plane)<props="intl">[ACK Pro provisioned control plane](https://www.alibabacloud.com/help/ack/ack-managed-and-ack-dedicated/user-guide/ack-pro-provisioned-control-plane). By pre-allocating and dedicating control plane resources, these tiers ensure consistently high levels of API concurrency and pod scheduling capabilities. They are suitable for AI training and inference, ultra-large-scale clusters, and mission-critical workloads.
        # 
        # For information about the cluster management fees for the Pro Edition and provisioned control plane editions, see <props="china">[Cluster management fees](https://help.aliyun.com/ack/ack-managed-and-ack-dedicated/product-overview/cluster-management-fee)<props="intl">[Cluster management fees](https://www.alibabacloud.com/help/ack/ack-managed-and-ack-dedicated/product-overview/cluster-management-fee).
        self.cluster_spec = cluster_spec
        # The cluster type. Valid values:
        # - Kubernetes: ACK dedicated cluster.
        # - ManagedKubernetes: ACK managed clusters, including ACK managed clusters (Pro Edition and Basic Edition), ACK Serverless clusters (Pro Edition and Basic Edition), ACK Edge clusters (Pro Edition and Basic Edition), and ACK Lingjun clusters (Pro Edition).
        # - ExternalKubernetes: registered cluster.
        self.cluster_type = cluster_type
        # The cluster name. Fuzzy match is supported.
        self.name = name
        # The page number of the current page.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The cluster subtype. This parameter is valid only when cluster_type is set to ManagedKubernetes. Valid values:
        # - Default: ACK serverless clusters, including ACK serverless cluster Pro Edition and Basic Edition.
        # - Edge: ACK Edge clusters, including ACK Edge cluster Pro Edition and Basic Edition.
        # - Serverless: ACK ACK clusters, including ACK ACK cluster Pro Edition and Basic Edition.
        # - Lingjun: ACK Lingjun clusters, providing Pro Edition.
        self.profile = profile
        # The region of the cluster. Specify this parameter to filter clusters by region.
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

