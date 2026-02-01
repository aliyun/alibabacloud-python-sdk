# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeAgentForClusterRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_version: str = None,
        cluster_id: str = None,
    ):
        self.agent_id = agent_id
        self.agent_version = agent_version
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agent_id'] = self.agent_id

        if self.agent_version is not None:
            result['agent_version'] = self.agent_version

        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_id') is not None:
            self.agent_id = m.get('agent_id')

        if m.get('agent_version') is not None:
            self.agent_version = m.get('agent_version')

        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        return self

