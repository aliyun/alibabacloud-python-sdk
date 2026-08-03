# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInsightsEventsCountRequest(DaraModel):
    def __init__(
        self,
        date: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The date to query. The format is `yyyy-MM-dd`.
        self.date = date
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        # 
        # > - - If Date, StartTime, and EndTime are all left empty, the system queries the number of events in the last 24 hours.
        # >
        # >   - If Date is specified, the StartTime and EndTime parameters are ignored. The system queries the number of events on the specified date.
        # >
        # >   - If Date is left empty and both StartTime and EndTime are specified, the system queries the number of events in the specified time range.
        self.end_time = end_time
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

