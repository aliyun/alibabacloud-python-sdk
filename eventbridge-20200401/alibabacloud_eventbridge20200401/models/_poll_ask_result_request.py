# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PollAskResultRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        message_id: str = None,
    ):
        # This parameter is required.
        self.agent_name = agent_name
        # This parameter is required.
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        return self

