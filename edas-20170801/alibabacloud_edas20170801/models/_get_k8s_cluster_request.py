# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetK8sClusterRequest(DaraModel):
    def __init__(
        self,
        cluster_type: int = None,
        current_page: int = None,
        page_size: int = None,
        region_tag: str = None,
        sub_cluster_type: str = None,
    ):
        # The type of the Kubernetes cluster:
        # 
        # - 5: an ACK cluster.
        # 
        # - 7: a self-managed Kubernetes cluster.
        self.cluster_type = cluster_type
        # The number of the page to return for a paged query. The default value is 1.
        self.current_page = current_page
        # The number of entries to return on each page for a paged query. The default value is 1000.
        self.page_size = page_size
        # The region.
        # 
        # This parameter is required.
        self.region_tag = region_tag
        # The subtype of the cluster:
        # 
        # - Ask: an ASK cluster.
        # 
        # - ManagedKubernetes: an ACK cluster.
        self.sub_cluster_type = sub_cluster_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_tag is not None:
            result['RegionTag'] = self.region_tag

        if self.sub_cluster_type is not None:
            result['SubClusterType'] = self.sub_cluster_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionTag') is not None:
            self.region_tag = m.get('RegionTag')

        if m.get('SubClusterType') is not None:
            self.sub_cluster_type = m.get('SubClusterType')

        return self

