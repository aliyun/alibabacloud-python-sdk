# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_searchagent20260515 import models as main_models
from darabonba.model import DaraModel

class ExecuteAcpCommandResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ExecuteAcpCommandResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

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
            temp_model = main_models.ExecuteAcpCommandResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self



class ExecuteAcpCommandResponseBodyData(DaraModel):
    def __init__(
        self,
        id: str = None,
        jsonrpc: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
        timestamp: int = None,
    ):
        self.id = id
        self.jsonrpc = jsonrpc
        self.request_id = request_id
        self.result = result
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.jsonrpc is not None:
            result['jsonrpc'] = self.jsonrpc

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('jsonrpc') is not None:
            self.jsonrpc = m.get('jsonrpc')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

