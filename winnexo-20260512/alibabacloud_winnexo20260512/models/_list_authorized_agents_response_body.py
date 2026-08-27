# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAuthorizedAgentsResponseBody(DaraModel):
    def __init__(
        self,
        agent_names: List[str] = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The agent names.
        self.agent_names = agent_names
        # The status code.
        self.code = code
        # The description of the status code.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_names is not None:
            result['agentNames'] = self.agent_names

        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentNames') is not None:
            self.agent_names = m.get('agentNames')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

