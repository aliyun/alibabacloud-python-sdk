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
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The specification of the cluster. Valid values:
        # 
        # - `ack.standard`: Standard Edition
        # 
        # - `ack.pro.small`: Pro Edition
        # 
        # - `ack.pro.xlarge`: Pro XL
        # 
        # - `ack.pro.2xlarge`: Pro 2XL
        # 
        # - `ack.pro.4xlarge`: Pro 4XL (To use this specification, you must submit a ticket.)
        # 
        # Pro XL, Pro 2XL, and Pro 4XL are three specifications available for the <props="china">[ACK Pro provisioned control plane](https://help.aliyun.com/ack/ack-managed-and-ack-dedicated/user-guide/ack-pro-provisioned-control-plane)<props="intl">[ACK Pro provisioned control plane](https://www.alibabacloud.com/help/ack/ack-managed-and-ack-dedicated/user-guide/ack-pro-provisioned-control-plane). These specifications ensure a high and deterministic level of API concurrency and Pod scheduling capabilities by pre-allocating and dedicating control plane resources. They are suitable for AI training and inference, large-scale clusters, and mission-critical workloads.
        # 
        # For information about the cluster management fees for Pro Edition and provisioned control plane clusters, see <props="china">[cluster management fee](https://help.aliyun.com/ack/ack-managed-and-ack-dedicated/product-overview/cluster-management-fee)<props="intl">[cluster management fee](https://www.alibabacloud.com/help/ack/ack-managed-and-ack-dedicated/product-overview/cluster-management-fee).
        self.cluster_spec = cluster_spec
        # The type of the cluster. Valid values:
        # 
        # - `Kubernetes`: an ACK dedicated cluster.
        # 
        # - `ManagedKubernetes`: an ACK managed cluster. This includes ACK managed clusters (Pro and Standard Editions), ACK Serverless clusters (Pro and Standard Editions), ACK Edge clusters (Pro and Standard Editions), and ACK Lingjun clusters (Pro Edition).
        # 
        # - `ExternalKubernetes`: a registered cluster.
        self.cluster_type = cluster_type
        # The name of the cluster. Fuzzy search is supported.
        self.name = name
        # The page number to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The subtype of the cluster. Valid values:
        # 
        # - `Default`: ACK managed clusters, including Pro and Standard Editions.
        # 
        # - `Edge`: ACK Edge clusters, including Pro and Standard Editions.
        # 
        # - `Serverless`: ACK Serverless clusters, including Pro and Standard Editions.
        # 
        # - `LingJun`: ACK Lingjun clusters, available in the Pro Edition.
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

