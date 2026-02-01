# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListClusterAgentInstallRecordsRequest(DaraModel):
    def __init__(
        self,
        agent_config_id: str = None,
        cluster_id: str = None,
        current: int = None,
        page_size: int = None,
        plugin_id: str = None,
        plugin_version: str = None,
    ):
        self.agent_config_id = agent_config_id
        self.cluster_id = cluster_id
        self.current = current
        self.page_size = page_size
        self.plugin_id = plugin_id
        self.plugin_version = plugin_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        return self

