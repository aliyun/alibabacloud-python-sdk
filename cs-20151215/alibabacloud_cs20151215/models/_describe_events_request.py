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
        # The maximum number of results returned per request.
        self.max_results = max_results
        # The query token. Set this parameter to the NextToken value returned by the previous API call.
        self.next_token = next_token
        # The page number for the paged query.
        self.page_number = page_number
        # The maximum number of results to return per page.
        # 
        # Valid values: [1,100].
        # 
        # Default value: 50.
        self.page_size = page_size
        # The event type. If you do not set this parameter, all types of events are queried. Valid values:
        # - `cluster_create`: creates a cluster.
        # - `cluster_scaleout`: scales out a cluster.
        # - `cluster_attach`: adds existing nodes.
        # - `cluster_delete`: deletes a cluster.
        # - `cluster_upgrade`: upgrades a cluster.
        # - `cluster_migrate`: migrates a cluster.
        # - `cluster_node_delete`: removes nodes.
        # - `cluster_node_drain`: drains nodes.
        # - `cluster_modify`: modifies a cluster.
        # - `cluster_configuration_modify`: modifies cluster management configurations.
        # - `cluster_addon_install`: installs a component.
        # - `cluster_addon_upgrade`: upgrades a component.
        # - `cluster_addon_uninstall`: uninstalls a component.
        # - `runtime_upgrade`: upgrades the runtime.
        # - `nodepool_upgrade`: upgrades a node pool.
        # - `nodepool_update`: updates a node pool.
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

