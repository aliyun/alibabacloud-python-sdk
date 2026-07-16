# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetScheduledReportsRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        scheduled_id: str = None,
        start_time: str = None,
    ):
        # The end time of the query range. The time must be in the YYYY-MM-DDTHH:mm:ssZ format.
        self.end_time = end_time
        # The page number. The default value is 1.
        self.page_number = page_number
        # The number of entries per page. The default value is 20, and the maximum value is 100.
        self.page_size = page_size
        # The ID of the inspection task.
        # 
        # This parameter is required.
        self.scheduled_id = scheduled_id
        # The start time of the query range. The time must be in the YYYY-MM-DDTHH:mm:ssZ format.
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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.scheduled_id is not None:
            result['ScheduledId'] = self.scheduled_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ScheduledId') is not None:
            self.scheduled_id = m.get('ScheduledId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

