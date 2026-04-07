# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListShiftSchedulesRequest(DaraModel):
    def __init__(
        self,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        shift_schedule_name: str = None,
    ):
        # The Alibaba Cloud account ID. You can log on to the DataWorks console and move the pointer over the profile picture in the upper-right corner to view the ID.
        self.owner = owner
        # The page number. Minimum value:1. Maximum value: 100. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The keyword used to perform a fuzzy search on shift schedules.
        self.shift_schedule_name = shift_schedule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner is not None:
            result['Owner'] = self.owner

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.shift_schedule_name is not None:
            result['ShiftScheduleName'] = self.shift_schedule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ShiftScheduleName') is not None:
            self.shift_schedule_name = m.get('ShiftScheduleName')

        return self

