# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClusterNodesRequest(DaraModel):
    def __init__(
        self,
        instance_ids: str = None,
        nodepool_id: str = None,
        page_number: str = None,
        page_size: str = None,
        state: str = None,
    ):
        # The IDs of the nodes that you want to query. Separate multiple node IDs with commas (,).
        self.instance_ids = instance_ids
        # The node pool ID.
        self.nodepool_id = nodepool_id
        # The page number.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The node state that you want to use to filter nodes. Valid values:
        # 
        # *   `all`: query nodes in the following four states.
        # *   `running`: query nodes in the running state.
        # *   `removing`: query nodes that are being removed.
        # *   `initial`: query nodes that are being initialized.
        # *   `failed`: query nodes that fail to be created.
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

        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('state') is not None:
            self.state = m.get('state')

        return self

