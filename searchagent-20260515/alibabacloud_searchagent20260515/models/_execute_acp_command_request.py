# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ExecuteAcpCommandRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        id: str = None,
        jsonrpc: str = None,
        method: str = None,
        params: Dict[str, Any] = None,
    ):
        self.agent_name = agent_name
        self.id = id
        self.jsonrpc = jsonrpc
        self.method = method
        self.params = params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['agentName'] = self.agent_name

        if self.id is not None:
            result['id'] = self.id

        if self.jsonrpc is not None:
            result['jsonrpc'] = self.jsonrpc

        if self.method is not None:
            result['method'] = self.method

        if self.params is not None:
            result['params'] = self.params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentName') is not None:
            self.agent_name = m.get('agentName')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('jsonrpc') is not None:
            self.jsonrpc = m.get('jsonrpc')

        if m.get('method') is not None:
            self.method = m.get('method')

        if m.get('params') is not None:
            self.params = m.get('params')

        return self

