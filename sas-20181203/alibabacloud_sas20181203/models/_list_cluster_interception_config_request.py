# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListClusterInterceptionConfigRequest(DaraModel):
    def __init__(
        self,
        cluster_cnnfstatus: int = None,
        cluster_id: str = None,
        cluster_name: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        # The status of the container firewall feature. Valid values:
        # 
        # *   **-1**: unknown
        # *   **0**: abnormal
        # *   **1**: normal
        # *   **2**: normal to be confirmed
        self.cluster_cnnfstatus = cluster_cnnfstatus
        # The ID of the cluster.
        # 
        # > You can call the [DescribeContainerInstances](~~DescribeContainerInstances~~) operation to query the IDs of clusters.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The number of the page to return. Default value: 1.
        self.current_page = current_page
        # The number of entries to return on each page. Default value: 20.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_cnnfstatus is not None:
            result['ClusterCNNFStatus'] = self.cluster_cnnfstatus

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterCNNFStatus') is not None:
            self.cluster_cnnfstatus = m.get('ClusterCNNFStatus')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

