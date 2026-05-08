# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FindGuestTicketRecordRequest(DaraModel):
    def __init__(
        self,
        activity_id: str = None,
        date_time_string: str = None,
        end_date_time: str = None,
        start_date_time: str = None,
    ):
        self.activity_id = activity_id
        self.date_time_string = date_time_string
        self.end_date_time = end_date_time
        self.start_date_time = start_date_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.date_time_string is not None:
            result['DateTimeString'] = self.date_time_string

        if self.end_date_time is not None:
            result['EndDateTime'] = self.end_date_time

        if self.start_date_time is not None:
            result['StartDateTime'] = self.start_date_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('DateTimeString') is not None:
            self.date_time_string = m.get('DateTimeString')

        if m.get('EndDateTime') is not None:
            self.end_date_time = m.get('EndDateTime')

        if m.get('StartDateTime') is not None:
            self.start_date_time = m.get('StartDateTime')

        return self

