# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListClusterAgentInstallRecordsRequest(DaraModel):
    def __init__(
        self,
        x_debug_id: str = None,
        agent_config_id: str = None,
        cluster_id: str = None,
        current: int = None,
        page_size: int = None,
        plugin_id: str = None,
        plugin_version: str = None,
        x_sysom_invoke_source: str = None,
    ):
        self.x_debug_id = x_debug_id
        self.agent_config_id = agent_config_id
        # Filters by cluster ID.
        # 
        # > This cluster ID is not the ACK cluster ID. It is the `cluster_id` field in the data returned by this operation, or the `id` field in the data returned by the ListCluster operation.
        self.cluster_id = cluster_id
        # The current page number (starting from 1).
        self.current = current
        # The number of entries per page.
        self.page_size = page_size
        # Specifies the agent ID to filter the installation list for the specified agent. This parameter can be used together with the plugin_version parameter.
        self.plugin_id = plugin_id
        # Cannot be used alone. Use this parameter together with plugin_id to filter the installation list for a specified version of the specified agent.
        self.plugin_version = plugin_version
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

        if self.agent_config_id is not None:
            result['agent_config_id'] = self.agent_config_id

        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.current is not None:
            result['current'] = self.current

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.plugin_id is not None:
            result['plugin_id'] = self.plugin_id

        if self.plugin_version is not None:
            result['plugin_version'] = self.plugin_version

        if self.x_sysom_invoke_source is not None:
            result['x-sysom-invoke-source'] = self.x_sysom_invoke_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Debug-Id') is not None:
            self.x_debug_id = m.get('X-Debug-Id')

        if m.get('agent_config_id') is not None:
            self.agent_config_id = m.get('agent_config_id')

        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('current') is not None:
            self.current = m.get('current')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('plugin_id') is not None:
            self.plugin_id = m.get('plugin_id')

        if m.get('plugin_version') is not None:
            self.plugin_version = m.get('plugin_version')

        if m.get('x-sysom-invoke-source') is not None:
            self.x_sysom_invoke_source = m.get('x-sysom-invoke-source')

        return self

