# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDDoSBpsMaxResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        max_atk_bps: int = None,
        max_atk_pps: int = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.max_atk_bps = max_atk_bps
        self.max_atk_pps = max_atk_pps
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.max_atk_bps is not None:
            result['MaxAtkBps'] = self.max_atk_bps

        if self.max_atk_pps is not None:
            result['MaxAtkPps'] = self.max_atk_pps

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MaxAtkBps') is not None:
            self.max_atk_bps = m.get('MaxAtkBps')

        if m.get('MaxAtkPps') is not None:
            self.max_atk_pps = m.get('MaxAtkPps')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

