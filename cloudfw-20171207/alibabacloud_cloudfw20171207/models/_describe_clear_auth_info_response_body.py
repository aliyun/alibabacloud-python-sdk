# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClearAuthInfoResponseBody(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        left_times: int = None,
        request_id: str = None,
    ):
        self.end_time = end_time
        self.left_times = left_times
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.left_times is not None:
            result['LeftTimes'] = self.left_times

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('LeftTimes') is not None:
            self.left_times = m.get('LeftTimes')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

