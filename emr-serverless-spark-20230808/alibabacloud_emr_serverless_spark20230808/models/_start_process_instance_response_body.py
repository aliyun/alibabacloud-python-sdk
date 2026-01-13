# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class StartProcessInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: Any = None,
        failed: bool = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The code that is returned by the backend server.
        self.code = code
        # The data returned.
        self.data = data
        # Indicates whether the workflow fails to be run manually.
        self.failed = failed
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The description of the returned code.
        self.msg = msg
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

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

        if self.failed is not None:
            result['failed'] = self.failed

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.msg is not None:
            result['msg'] = self.msg

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('failed') is not None:
            self.failed = m.get('failed')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('msg') is not None:
            self.msg = m.get('msg')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

