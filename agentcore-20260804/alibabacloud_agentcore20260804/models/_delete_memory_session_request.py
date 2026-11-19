# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMemorySessionRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        team_id: str = None,
        user_id: str = None,
    ):
        # agentId
        self.agent_id = agent_id
        # teamId
        self.team_id = team_id
        # userId
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.team_id is not None:
            result['teamId'] = self.team_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('teamId') is not None:
            self.team_id = m.get('teamId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

