# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CeaseFunctionInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: int = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The error code.
        self.code = code
        # The HTTP status code.
        self.http_code = http_code
        # The latency in minutes.
        self.latency = latency
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The request status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.latency is not None:
            result['latency'] = self.latency

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('latency') is not None:
            self.latency = m.get('latency')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

