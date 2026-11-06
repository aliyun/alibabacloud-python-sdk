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
    ):
        # The `Error` field in the frame. This is an in-stream error, which is an object.
        self.error = error
        # The `Id` field in the frame, used to associate the request. Notification frames may not contain this field.
        self.id = id
        # The `Jsonrpc` field in the frame. The value is `2.0`.
        self.jsonrpc = jsonrpc
        # The `Method` field in the frame, used to distinguish notification categories.
        self.method = method
        # The `Params` field in the frame. This is the notification payload, which is an object.
        self.params = params
        # The request diagnostic identifier. This identifier is not guaranteed to be included in every frame. You should also retain the diagnostic information in the response headers.
        self.request_id = request_id
        # The `Result` field in the frame. This is the normal result, which is an object.
        self.result = result

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

        return self

