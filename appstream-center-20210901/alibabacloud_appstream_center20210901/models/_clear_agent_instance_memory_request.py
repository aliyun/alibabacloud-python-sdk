# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ClearAgentInstanceMemoryRequest(DaraModel):
    def __init__(
        self,
        agent_instance_id: str = None,
    ):
        # The ID of the agent instance whose memory you want to clear. This parameter is required and can be obtained from the response of ListAgentInstanceMemory.
        self.agent_instance_id = agent_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_instance_id is not None:
            result['AgentInstanceId'] = self.agent_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentInstanceId') is not None:
            self.agent_instance_id = m.get('AgentInstanceId')

        return self

