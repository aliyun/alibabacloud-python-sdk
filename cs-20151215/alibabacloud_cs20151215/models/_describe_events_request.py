# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEventsRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
        type: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The event type. Valid values:
        # 
        # *   `cluster_create`: cluster creation.
        # *   `cluster_scaleout`: cluster scale-out.
        # *   `cluster_attach`: node addition.
        # *   `cluster_delete`: cluster deletion.
        # *   `cluster_upgrade`: cluster upgrades.
        # *   `cluster_migrate`: cluster migration.
        # *   `cluster_node_delete`: node removal.
        # *   `cluster_node_drain`: node draining.
        # *   `cluster_modify`: cluster modifications.
        # *   `cluster_configuration_modify`: modifications of control plane configurations.
        # *   `cluster_addon_install`: component installation.
        # *   `cluster_addon_upgrade`: component updates.
        # *   `cluster_addon_uninstall`: component uninstallation.
        # *   `runtime_upgrade`: runtime updates.
        # *   `nodepool_upgrade`: node pool upgrades.
        # *   `nodepool_update`: node pool updates.
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

        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

