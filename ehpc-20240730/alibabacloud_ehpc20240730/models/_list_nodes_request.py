# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListNodesRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        hostnames: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        private_ip_address: List[str] = None,
        queue_names: List[str] = None,
        sequence: str = None,
        sort_by: str = None,
        status: List[str] = None,
    ):
        # The cluster ID. You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the cluster ID.
        self.cluster_id = cluster_id
        # The hostnames of the compute nodes that you want to query.
        self.hostnames = hostnames
        # The page number of the page to return.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The IP addresses of the compute nodes that you want to query.
        self.private_ip_address = private_ip_address
        # The queues to which the nodes belong.
        self.queue_names = queue_names
        # Specifies whether the results are sorted in ascending or descending order. Valid values:
        # 
        # *   Forward: ascending
        # *   Backward: descending
        # 
        # Default value: Forward.
        self.sequence = sequence
        # The sorting method of the node list. Valid values:
        # 
        # *   AddedTime: sorts the nodes by the time that they were added.
        # *   HostName: sorts the nodes by their hostnames.
        # 
        # Default value: addedtime.
        self.sort_by = sort_by
        # The states of the compute nodes to be queried.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.hostnames is not None:
            result['Hostnames'] = self.hostnames

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.queue_names is not None:
            result['QueueNames'] = self.queue_names

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Hostnames') is not None:
            self.hostnames = m.get('Hostnames')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('QueueNames') is not None:
            self.queue_names = m.get('QueueNames')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

