# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEnsResourceUsageRequest(DaraModel):
    def __init__(
        self,
        expired_end_time: str = None,
        expired_start_time: str = None,
    ):
        # The end of the time range to query. Format: yyyy-MM-dd or yyyy-MM-dd HH:mm:ss.
        self.expired_end_time = expired_end_time
        # The beginning of the time range to query. Format: yyyy-MM-dd or yyyy-MM-dd HH:mm:ss.
        self.expired_start_time = expired_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expired_end_time is not None:
            result['ExpiredEndTime'] = self.expired_end_time

        if self.expired_start_time is not None:
            result['ExpiredStartTime'] = self.expired_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredEndTime') is not None:
            self.expired_end_time = m.get('ExpiredEndTime')

        if m.get('ExpiredStartTime') is not None:
            self.expired_start_time = m.get('ExpiredStartTime')

        return self

