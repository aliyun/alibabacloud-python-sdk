# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportAgentJobsRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        cluster_id: str = None,
        migrate_strategy: int = None,
    ):
        # This parameter is required.
        self.agent_name = agent_name
        # This parameter is required.
        self.cluster_id = cluster_id
        self.migrate_strategy = migrate_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.migrate_strategy is not None:
            result['MigrateStrategy'] = self.migrate_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('MigrateStrategy') is not None:
            self.migrate_strategy = m.get('MigrateStrategy')

        return self

