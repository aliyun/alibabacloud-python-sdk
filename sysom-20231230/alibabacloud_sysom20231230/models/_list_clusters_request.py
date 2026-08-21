# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListClustersRequest(DaraModel):
    def __init__(
        self,
        x_debug_id: str = None,
        cluster_id: str = None,
        cluster_status: str = None,
        cluster_type: str = None,
        current: int = None,
        id: str = None,
        name: str = None,
        page_size: int = None,
        x_sysom_invoke_source: str = None,
    ):
        self.x_debug_id = x_debug_id
        # Filters by cluster ID.
        # 
        # > This cluster ID is not the ACK cluster ID. It is the `id` field returned by this operation.
        self.cluster_id = cluster_id
        # - `Running`: The cluster is managed normally.
        # - `Installing`: An installation task is in progress for the cluster.
        # - `Uninstalling`: An uninstallation task is in progress for the cluster.
        # - `Upgrading`: An update task is in progress for the cluster.
        # - `Offline`: The cluster is offline and management is abnormal.
        self.cluster_status = cluster_status
        # - `ACK`: ACK cluster.
        # - `CUSTOM`: Custom cluster (default clusters belong to custom clusters).
        self.cluster_type = cluster_type
        # The current page number (starting from page 1).
        self.current = current
        # **[Deprecated]** Use the cluster_id parameter to filter instead.
        self.id = id
        # Filters plugins by plugin name.
        self.name = name
        # The number of entries per page.
        self.page_size = page_size
        self.x_sysom_invoke_source = x_sysom_invoke_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_debug_id is not None:
            result['X-Debug-Id'] = self.x_debug_id

        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.cluster_status is not None:
            result['cluster_status'] = self.cluster_status

        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type

        if self.current is not None:
            result['current'] = self.current

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.x_sysom_invoke_source is not None:
            result['x-sysom-invoke-source'] = self.x_sysom_invoke_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Debug-Id') is not None:
            self.x_debug_id = m.get('X-Debug-Id')

        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('cluster_status') is not None:
            self.cluster_status = m.get('cluster_status')

        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')

        if m.get('current') is not None:
            self.current = m.get('current')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('x-sysom-invoke-source') is not None:
            self.x_sysom_invoke_source = m.get('x-sysom-invoke-source')

        return self

