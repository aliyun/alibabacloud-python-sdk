# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClusterNodesRequest(DaraModel):
    def __init__(
        self,
        instance_ids: str = None,
        node_ips: str = None,
        node_labels: str = None,
        node_names: str = None,
        nodepool_id: str = None,
        page_number: str = None,
        page_size: str = None,
        state: str = None,
    ):
        # The list of node instance IDs. Separate multiple values with commas (,).
        self.instance_ids = instance_ids
        # The list of node IP addresses used for filtering. Separate multiple values with commas (,).
        self.node_ips = node_ips
        # The node labels used for filtering. Specify the labels as key=value pairs separated by commas (,). Multiple labels are evaluated with the AND operator. Only nodes that match all specified labels are returned.
        self.node_labels = node_labels
        # The list of node names used for filtering. Separate multiple values with commas (,).
        self.node_names = node_names
        # The node pool ID.
        self.nodepool_id = nodepool_id
        # The page number of the current query.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The maximum number of records to return per page. Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The running states of the cluster nodes used for filtering. Valid values:
        # 
        # - `all`: does not filter nodes by running state and queries nodes in all states.
        # - `running`: the cluster nodes that are running.
        # - `removing`: the cluster nodes that are being removed.
        # - `initial`: the cluster nodes that are being initialized.
        # - `failed`: the cluster nodes that failed to be created.
        # 
        # Default value: `all`.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids

        if self.node_ips is not None:
            result['nodeIps'] = self.node_ips

        if self.node_labels is not None:
            result['nodeLabels'] = self.node_labels

        if self.node_names is not None:
            result['nodeNames'] = self.node_names

        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.state is not None:
            result['state'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')

        if m.get('nodeIps') is not None:
            self.node_ips = m.get('nodeIps')

        if m.get('nodeLabels') is not None:
            self.node_labels = m.get('nodeLabels')

        if m.get('nodeNames') is not None:
            self.node_names = m.get('nodeNames')

        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('state') is not None:
            self.state = m.get('state')

        return self

