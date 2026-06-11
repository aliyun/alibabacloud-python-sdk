# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetChatContentRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        checkpoint: str = None,
        dmsunit: str = None,
        session_id: str = None,
    ):
        # The agent ID. This parameter is required.
        self.agent_id = agent_id
        # The service returns output starting from this checkpoint.
        self.checkpoint = checkpoint
        # The DMS unit. For users on the Alibaba Cloud China site, the default value is cn-hangzhou.
        self.dmsunit = dmsunit
        # The session ID. This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint

        if self.dmsunit is not None:
            result['DMSUnit'] = self.dmsunit

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')

        if m.get('DMSUnit') is not None:
            self.dmsunit = m.get('DMSUnit')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

