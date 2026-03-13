# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TravelStandardRelateDeleteResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result_code: int = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result_code = result_code
        self.success = success
        # traceId
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result_code is not None:
            result['resultCode'] = self.result_code

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resultCode') is not None:
            self.result_code = m.get('resultCode')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

