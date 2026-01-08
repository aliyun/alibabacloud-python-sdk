# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInvadeEventStatisticResponseBody(DaraModel):
    def __init__(
        self,
        high_open_event_cnt: int = None,
        low_open_event_cnt: int = None,
        middle_open_event_cnt: int = None,
        request_id: str = None,
        total_open_event_cnt: int = None,
    ):
        self.high_open_event_cnt = high_open_event_cnt
        self.low_open_event_cnt = low_open_event_cnt
        self.middle_open_event_cnt = middle_open_event_cnt
        self.request_id = request_id
        self.total_open_event_cnt = total_open_event_cnt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.high_open_event_cnt is not None:
            result['HighOpenEventCnt'] = self.high_open_event_cnt

        if self.low_open_event_cnt is not None:
            result['LowOpenEventCnt'] = self.low_open_event_cnt

        if self.middle_open_event_cnt is not None:
            result['MiddleOpenEventCnt'] = self.middle_open_event_cnt

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_open_event_cnt is not None:
            result['TotalOpenEventCnt'] = self.total_open_event_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HighOpenEventCnt') is not None:
            self.high_open_event_cnt = m.get('HighOpenEventCnt')

        if m.get('LowOpenEventCnt') is not None:
            self.low_open_event_cnt = m.get('LowOpenEventCnt')

        if m.get('MiddleOpenEventCnt') is not None:
            self.middle_open_event_cnt = m.get('MiddleOpenEventCnt')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalOpenEventCnt') is not None:
            self.total_open_event_cnt = m.get('TotalOpenEventCnt')

        return self

