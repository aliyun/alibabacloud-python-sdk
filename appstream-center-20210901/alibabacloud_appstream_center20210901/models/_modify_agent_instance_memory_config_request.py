# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyAgentInstanceMemoryConfigRequest(DaraModel):
    def __init__(
        self,
        agent_instance_ids: List[str] = None,
        enabled: bool = None,
    ):
        # The list of agent instance IDs. You can specify 1 to 100 IDs, and the IDs must be unique. Each instance must belong to the current account, support memory management, and have the memory feature configured.
        self.agent_instance_ids = agent_instance_ids
        # Required. Specifies whether to enable the memory feature. Valid values:
        # - true: Enables the memory feature.
        # - false: Disables the memory feature.
        # Before you enable the feature, ensure that the tenant-level memory store is enabled.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_instance_ids is not None:
            result['AgentInstanceIds'] = self.agent_instance_ids

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentInstanceIds') is not None:
            self.agent_instance_ids = m.get('AgentInstanceIds')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        return self

