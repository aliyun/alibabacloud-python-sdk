# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryAskLumaLogRequest(DaraModel):
    def __init__(
        self,
        after: str = None,
        agent_name: str = None,
        limit: int = None,
    ):
        # The cursor. Set this parameter to the messageId of the last entry on the previous page.
        self.after = after
        # The agent name. If this parameter is not specified, logs of all agents are queried.
        self.agent_name = agent_name
        # The number of entries to return. Default value: 20. Maximum value: 50.
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after is not None:
            result['After'] = self.after

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.limit is not None:
            result['Limit'] = self.limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('After') is not None:
            self.after = m.get('After')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        return self

