# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UninstallAgentForClusterRequest(DaraModel):
    def __init__(
        self,
        x_debug_id: str = None,
        agent_id: str = None,
        agent_version: str = None,
        cluster_id: str = None,
        x_sysom_invoke_source: str = None,
    ):
        self.x_debug_id = x_debug_id
        # The component ID.
        self.agent_id = agent_id
        # The component version.
        self.agent_version = agent_version
        # The cluster ID.
        # 
        # > This cluster ID must be the ID of an ACK cluster.
        self.cluster_id = cluster_id
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

        if self.agent_id is not None:
            result['agent_id'] = self.agent_id

        if self.agent_version is not None:
            result['agent_version'] = self.agent_version

        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.x_sysom_invoke_source is not None:
            result['x-sysom-invoke-source'] = self.x_sysom_invoke_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Debug-Id') is not None:
            self.x_debug_id = m.get('X-Debug-Id')

        if m.get('agent_id') is not None:
            self.agent_id = m.get('agent_id')

        if m.get('agent_version') is not None:
            self.agent_version = m.get('agent_version')

        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('x-sysom-invoke-source') is not None:
            self.x_sysom_invoke_source = m.get('x-sysom-invoke-source')

        return self

