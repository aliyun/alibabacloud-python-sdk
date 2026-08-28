# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class InvokeAIAgentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.InvokeAIAgentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
            temp_model = main_models.InvokeAIAgentResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class InvokeAIAgentResponseBodyData(DaraModel):
    def __init__(
        self,
        body: str = None,
        headers: Dict[str, str] = None,
        http_code: int = None,
    ):
        self.body = body
        self.headers = headers
        self.http_code = http_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        if self.headers is not None:
            result['headers'] = self.headers

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        return self

