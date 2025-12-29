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
        # The specification of the clusters to query. Valid values:
        # 
        # *   ack.pro.small: ACK Pro clusters.
        # *   ack.standard: ACK Basic clusters.
        self.cluster_spec = cluster_spec
        # The type of the clusters to query. Valid values:
        # 
        # *   Kubernetes: ACK dedicated clusters.
        # *   ManagedKubernetes: ACK managed clusters. ACK managed clusters include ACK Basic clusters, ACK Pro clusters, ACK Serverless Basic clusters, ACK Serverless Pro clusters, ACK Edge Basic clusters, ACK Edge Pro clusters, and ACK Lingjun Pro clusters.
        # *   ExternalKubernetes: registered clusters.
        self.cluster_type = cluster_type
        # Perform a fuzzy search by using the cluster name.
        self.name = name
        # The number of pages.
        self.page_number = page_number
        # The number of records on each page.
        self.page_size = page_size
        # The subtype of the clusters to query. Valid values:
        # 
        # *   Default: ACK managed clusters. ACK managed clusters include ACK Basic clusters and ACK Pro clusters.
        # *   Edge: ACK Edge clusters. ACK Edge clusters include ACK Edge Basic clusters and ACK Edge Pro clusters.
        # *   Serverless: ACK Serverless clusters. ACK Serverless clusters include ACK Serverless Basic clusters and ACK Serverless Pro clusters.
        # *   Lingjun: ACK Lingjun Pro clusters.
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

