# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class LoadAgentSessionResponseBody(DaraModel):
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
        # The error object of the SSE frame. This field is present when an error occurs.
        self.error = error
        # The client-generated request ID, returned from the request.
        self.id = id
        # The JSON-RPC version. The value is `2.0`.
        self.jsonrpc = jsonrpc
        # The method of the SSE frame.
        self.method = method
        # The parameters of the SSE frame.
        self.params = params
        # The unique request ID generated for this request.
        self.request_id = request_id
        # The result object of the SSE frame. This field is present when the operation is successful.
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

