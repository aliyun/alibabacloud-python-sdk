# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAttackProtectionCountRequest(DaraModel):
    def __init__(
        self,
        agent_type: str = None,
        end_timestamp: int = None,
        start_timestamp: int = None,
    ):
        self.agent_type = agent_type
        # This parameter is required.
        self.end_timestamp = end_timestamp
        # This parameter is required.
        self.start_timestamp = start_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_type is not None:
            result['AgentType'] = self.agent_type

        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')

        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        return self

