# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class PromptAgentSessionResponseBody(DaraModel):
    def __init__(
        self,
        error: Any = None,
        id: str = None,
        jsonrpc: str = None,
        method: str = None,
        params: Any = None,
        request_id: str = None,
        result: Any = None,
        timestamp: int = None,
    ):
        # The error information returned in the SSE frame. The response content conforms to the open-source Agent Client Protocol (ACP) specification. For more information, see https\\://agentclientprotocol.com/protocol/prompt-turn
        self.error = error
        # The ID passed in by the caller. The value is returned as-is in the response.
        self.id = id
        # The JSON-RPC version. Fixed value: 2.0.
        self.jsonrpc = jsonrpc
        # The SSE method. The response content conforms to the open-source Agent Client Protocol (ACP) specification. For more information, see https\\://agentclientprotocol.com/protocol/prompt-turn
        self.method = method
        # The SSE params. The response content conforms to the open-source Agent Client Protocol (ACP) specification. For more information, see https\\://agentclientprotocol.com/protocol/prompt-turn
        self.params = params
        # Id of the request
        self.request_id = request_id
        # The SSE frame result set. The response content conforms to the open-source Agent Client Protocol (ACP) specification. For more information, see https\\://agentclientprotocol.com/protocol/prompt-turn
        self.result = result
        # The timestamp.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error is not None:
            result['Error'] = self.error

        if self.id is not None:
            result['Id'] = self.id

        if self.jsonrpc is not None:
            result['Jsonrpc'] = self.jsonrpc

        if self.method is not None:
            result['Method'] = self.method

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Jsonrpc') is not None:
            self.jsonrpc = m.get('Jsonrpc')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

