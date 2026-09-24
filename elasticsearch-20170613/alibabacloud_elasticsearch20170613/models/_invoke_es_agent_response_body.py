# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class InvokeEsAgentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, str] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code. A value of 200 indicates a successful call. For non-200 values, the message field contains the error description.
        self.code = code
        # The JSON-RPC 2.0 response body. data.result contains the actual return content of the called ACP method. data.id is the id passed in the request. data.jsonrpc is fixed to 2.0. data.timestamp is the UNIX timestamp in milliseconds when the response was generated.
        self.data = data
        # The error description. The value is null when the call is successful. A specific error message is returned when the call fails.
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

