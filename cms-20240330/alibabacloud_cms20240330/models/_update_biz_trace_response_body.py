# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateBizTraceResponseBody(DaraModel):
    def __init__(
        self,
        biz_trace_id: str = None,
        request_id: str = None,
    ):
        self.biz_trace_id = biz_trace_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_trace_id is not None:
            result['bizTraceId'] = self.biz_trace_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizTraceId') is not None:
            self.biz_trace_id = m.get('bizTraceId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

