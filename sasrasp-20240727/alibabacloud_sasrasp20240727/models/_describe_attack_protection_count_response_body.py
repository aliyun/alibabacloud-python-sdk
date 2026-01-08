# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAttackProtectionCountResponseBody(DaraModel):
    def __init__(
        self,
        block_high_count: int = None,
        block_low_count: int = None,
        block_medium_count: int = None,
        monitor_high_count: int = None,
        monitor_low_count: int = None,
        monitor_medium_count: int = None,
        request_id: str = None,
        total_request_count: int = None,
    ):
        self.block_high_count = block_high_count
        self.block_low_count = block_low_count
        self.block_medium_count = block_medium_count
        self.monitor_high_count = monitor_high_count
        self.monitor_low_count = monitor_low_count
        self.monitor_medium_count = monitor_medium_count
        self.request_id = request_id
        self.total_request_count = total_request_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_high_count is not None:
            result['BlockHighCount'] = self.block_high_count

        if self.block_low_count is not None:
            result['BlockLowCount'] = self.block_low_count

        if self.block_medium_count is not None:
            result['BlockMediumCount'] = self.block_medium_count

        if self.monitor_high_count is not None:
            result['MonitorHighCount'] = self.monitor_high_count

        if self.monitor_low_count is not None:
            result['MonitorLowCount'] = self.monitor_low_count

        if self.monitor_medium_count is not None:
            result['MonitorMediumCount'] = self.monitor_medium_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_request_count is not None:
            result['TotalRequestCount'] = self.total_request_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockHighCount') is not None:
            self.block_high_count = m.get('BlockHighCount')

        if m.get('BlockLowCount') is not None:
            self.block_low_count = m.get('BlockLowCount')

        if m.get('BlockMediumCount') is not None:
            self.block_medium_count = m.get('BlockMediumCount')

        if m.get('MonitorHighCount') is not None:
            self.monitor_high_count = m.get('MonitorHighCount')

        if m.get('MonitorLowCount') is not None:
            self.monitor_low_count = m.get('MonitorLowCount')

        if m.get('MonitorMediumCount') is not None:
            self.monitor_medium_count = m.get('MonitorMediumCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRequestCount') is not None:
            self.total_request_count = m.get('TotalRequestCount')

        return self

