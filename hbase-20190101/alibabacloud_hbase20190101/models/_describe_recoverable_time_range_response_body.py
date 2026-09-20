# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRecoverableTimeRangeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        time_begin: str = None,
        time_end: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The start time of the recoverable time range.
        self.time_begin = time_begin
        # The end time of the recoverable time range.
        self.time_end = time_end

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.time_begin is not None:
            result['TimeBegin'] = self.time_begin

        if self.time_end is not None:
            result['TimeEnd'] = self.time_end

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TimeBegin') is not None:
            self.time_begin = m.get('TimeBegin')

        if m.get('TimeEnd') is not None:
            self.time_end = m.get('TimeEnd')

        return self

