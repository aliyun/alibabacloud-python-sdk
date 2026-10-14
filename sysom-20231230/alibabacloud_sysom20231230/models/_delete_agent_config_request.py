# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAgentConfigRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        config_id: str = None,
    ):
        # The ID of the component associated with the configuration to delete.
        self.agent_id = agent_id
        # The ID of the component configuration to delete.
        self.config_id = config_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.config_id is not None:
            result['configId'] = self.config_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('configId') is not None:
            self.config_id = m.get('configId')

        return self

