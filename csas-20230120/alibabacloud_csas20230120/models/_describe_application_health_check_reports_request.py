# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeApplicationHealthCheckReportsRequest(DaraModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        end_time: int = None,
        start_time: int = None,
    ):
        # The IDs of the internal-facing applications. You can specify up to 100 application IDs.
        # 
        # This parameter is required.
        self.application_ids = application_ids
        # The end time of the query. The value is a UNIX timestamp in seconds. If this parameter is not specified, the default value is the current time. If only the start time is specified, the end time is set to 5 minutes after the start time. The end time must be later than the start time, and the maximum query time range is 7 days.
        self.end_time = end_time
        # The start time of the query. The value is a UNIX timestamp in seconds. If this parameter is not specified, the default value is 5 minutes before the end time. If only the end time is specified, the start time is set to 5 minutes before the end time.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

