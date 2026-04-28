# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class CreateMemoryRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        enhancements: Dict[str, Any] = None,
        messages: Any = None,
        run_id: str = None,
        user_id: str = None,
    ):
        self.agent_id = agent_id
        self.enhancements = enhancements
        self.messages = messages
        self.run_id = run_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agent_id'] = self.agent_id

        if self.enhancements is not None:
            result['enhancements'] = self.enhancements

        if self.messages is not None:
            result['messages'] = self.messages

        if self.run_id is not None:
            result['run_id'] = self.run_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_id') is not None:
            self.agent_id = m.get('agent_id')

        if m.get('enhancements') is not None:
            self.enhancements = m.get('enhancements')

        if m.get('messages') is not None:
            self.messages = m.get('messages')

        if m.get('run_id') is not None:
            self.run_id = m.get('run_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

