# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class CreateAgentSessionRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        jsonrpc: str = None,
        params: Any = None,
    ):
        # The correlation identifier for this call. It is echoed in the response and does not provide idempotence guarantees.
        self.id = id
        # The JSON-RPC protocol version. Set the value to `2.0`.
        self.jsonrpc = jsonrpc
        # The business parameter object. For nested fields, see the supplementary description of request parameters.
        # 
        # This parameter is required.
        self.params = params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.jsonrpc is not None:
            result['Jsonrpc'] = self.jsonrpc

        if self.params is not None:
            result['Params'] = self.params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Jsonrpc') is not None:
            self.jsonrpc = m.get('Jsonrpc')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        return self

