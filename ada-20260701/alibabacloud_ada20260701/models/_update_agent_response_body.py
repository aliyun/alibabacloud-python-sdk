# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAgentResponseBody(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        name: str = None,
        request_id: str = None,
        success: bool = None,
        updated_at: int = None,
    ):
        # Agent ID。
        self.agent_id = agent_id
        # The Agent name.
        self.name = name
        # The request ID, used for Tracing Analysis and troubleshooting.
        self.request_id = request_id
        # Indicates whether the Agent was successfully updated. A successful response always returns `true`. A failure returns an error response.
        self.success = success
        # The most recent update time, as a UNIX timestamp in milliseconds.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self

