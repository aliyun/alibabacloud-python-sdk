# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgentSessionTokenUsageShrinkRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        jsonrpc: str = None,
        params_shrink: str = None,
    ):
        # The ID provided by the requester, which is echoed in the response.
        self.id = id
        # The JSON-RPC version. The value is always 2.0.
        self.jsonrpc = jsonrpc
        # Business parameters.
        self.params_shrink = params_shrink

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

        if self.params_shrink is not None:
            result['Params'] = self.params_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Jsonrpc') is not None:
            self.jsonrpc = m.get('Jsonrpc')

        if m.get('Params') is not None:
            self.params_shrink = m.get('Params')

        return self

