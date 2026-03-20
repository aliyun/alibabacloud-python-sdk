# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSchedulerxCalendarRequest(DaraModel):
    def __init__(
        self,
        calendar_name: str = None,
        month_days_content: str = None,
        region_id: str = None,
        year: int = None,
    ):
        # The calendar name.
        # 
        # This parameter is required.
        self.calendar_name = calendar_name
        # The month and days.
        # 
        # This parameter is required.
        self.month_days_content = month_days_content
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The year.
        # 
        # This parameter is required.
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calendar_name is not None:
            result['CalendarName'] = self.calendar_name

        if self.month_days_content is not None:
            result['MonthDaysContent'] = self.month_days_content

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.year is not None:
            result['Year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalendarName') is not None:
            self.calendar_name = m.get('CalendarName')

        if m.get('MonthDaysContent') is not None:
            self.month_days_content = m.get('MonthDaysContent')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Year') is not None:
            self.year = m.get('Year')

        return self

