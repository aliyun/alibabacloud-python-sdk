# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnbindPolarClawAgentResponseBody(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        application_id: str = None,
        code: int = None,
        message: str = None,
        removed_count: int = None,
        request_id: str = None,
        total_bindings: int = None,
    ):
        # The agent ID.
        self.agent_id = agent_id
        # The application ID.
        self.application_id = application_id
        # The status code of the response.
        self.code = code
        # The response message.
        self.message = message
        # The number of removed bindings.
        self.removed_count = removed_count
        # The request ID.
        self.request_id = request_id
        # The total number of bindings after the operation.
        self.total_bindings = total_bindings

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.removed_count is not None:
            result['RemovedCount'] = self.removed_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_bindings is not None:
            result['TotalBindings'] = self.total_bindings

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RemovedCount') is not None:
            self.removed_count = m.get('RemovedCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalBindings') is not None:
            self.total_bindings = m.get('TotalBindings')

        return self

