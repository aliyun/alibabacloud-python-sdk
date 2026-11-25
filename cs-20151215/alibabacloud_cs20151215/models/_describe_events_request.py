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
        # The maximum number of results to return for a single request.
        self.max_results = max_results
        # The query token, which is the value of the NextToken parameter returned by the previous API call.
        self.next_token = next_token
        # The page number for paging.
        self.page_number = page_number
        # The maximum number of results to return per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 50.
        self.page_size = page_size
        # The event type. If you do not specify this parameter, events of all types are queried. Valid values:
        # - `cluster_create`: cluster creation
        # - `cluster_scaleout`: cluster scale-out
        # - `cluster_attach`: adding existing nodes
        # - `cluster_delete`: cluster deletion
        # - `cluster_upgrade`: cluster upgrade
        # - `cluster_migrate`: cluster migration
        # - `cluster_node_delete`: node removal
        # - `cluster_node_drain`: node draining
        # - `cluster_modify`: cluster modification
        # - `cluster_configuration_modify`: cluster management configuration modification
        # - `cluster_addon_install`: add-on installation
        # - `cluster_addon_upgrade`: add-on upgrade
        # - `cluster_addon_uninstall`: add-on uninstallation
        # - `runtime_upgrade`: runtime upgrade
        # - `nodepool_upgrade`: node pool upgrade
        # - `nodepool_update`: node pool update
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

