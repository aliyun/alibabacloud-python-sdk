# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEventsRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        type: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The maximum number of results to return.
        self.max_results = max_results
        # The pagination token. Set this parameter to the value of `NextToken` returned by the previous API call.
        self.next_token = next_token
        # The number of the page to return.
        self.page_number = page_number
        # The maximum number of results per page.
        # 
        # Valid values: [1,100].
        # 
        # Default: 50.
        self.page_size = page_size
        # The event type. If you do not specify this parameter, events of all types are returned. Valid values:
        # 
        # - `cluster_create`: Create a cluster.
        # 
        # - `cluster_scaleout`: Scale out a cluster.
        # 
        # - `cluster_attach`: Attach an existing node.
        # 
        # - `cluster_delete`: Delete a cluster.
        # 
        # - `cluster_upgrade`: Upgrade a cluster.
        # 
        # - `cluster_migrate`: Migrate a cluster.
        # 
        # - `cluster_node_delete`: Remove a node.
        # 
        # - `cluster_node_drain`: Drain a node.
        # 
        # - `cluster_modify`: Modify a cluster.
        # 
        # - `cluster_configuration_modify`: Modify the control plane configuration of a cluster.
        # 
        # - `cluster_addon_install`: Install an add-on.
        # 
        # - `cluster_addon_upgrade`: Upgrade an add-on.
        # 
        # - `cluster_addon_uninstall`: Uninstall an add-on.
        # 
        # - `runtime_upgrade`: Upgrade the runtime.
        # 
        # - `nodepool_upgrade`: Upgrade a node pool.
        # 
        # - `nodepool_update`: Update a node pool.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.max_results is not None:
            result['max_results'] = self.max_results

        if self.next_token is not None:
            result['next_token'] = self.next_token

        if self.page_number is not None:
            result['page_number'] = self.page_number

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('max_results') is not None:
            self.max_results = m.get('max_results')

        if m.get('next_token') is not None:
            self.next_token = m.get('next_token')

        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

