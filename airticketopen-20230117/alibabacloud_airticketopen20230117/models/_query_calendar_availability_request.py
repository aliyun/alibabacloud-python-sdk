# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryCalendarAvailabilityRequest(DaraModel):
    def __init__(
        self,
        account_no: int = None,
        adult_count: int = None,
        check_in_date_end: str = None,
        check_in_date_start: str = None,
        child_count: int = None,
        children_ages: List[int] = None,
        room_count: int = None,
        standard_hotel_ids: List[str] = None,
        tracer_id: str = None,
    ):
        # This parameter is required.
        self.account_no = account_no
        # This parameter is required.
        self.adult_count = adult_count
        # This parameter is required.
        self.check_in_date_end = check_in_date_end
        # This parameter is required.
        self.check_in_date_start = check_in_date_start
        self.child_count = child_count
        self.children_ages = children_ages
        # This parameter is required.
        self.room_count = room_count
        # This parameter is required.
        self.standard_hotel_ids = standard_hotel_ids
        self.tracer_id = tracer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_no is not None:
            result['AccountNo'] = self.account_no

        if self.adult_count is not None:
            result['AdultCount'] = self.adult_count

        if self.check_in_date_end is not None:
            result['CheckInDateEnd'] = self.check_in_date_end

        if self.check_in_date_start is not None:
            result['CheckInDateStart'] = self.check_in_date_start

        if self.child_count is not None:
            result['ChildCount'] = self.child_count

        if self.children_ages is not None:
            result['ChildrenAges'] = self.children_ages

        if self.room_count is not None:
            result['RoomCount'] = self.room_count

        if self.standard_hotel_ids is not None:
            result['StandardHotelIds'] = self.standard_hotel_ids

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')

        if m.get('AdultCount') is not None:
            self.adult_count = m.get('AdultCount')

        if m.get('CheckInDateEnd') is not None:
            self.check_in_date_end = m.get('CheckInDateEnd')

        if m.get('CheckInDateStart') is not None:
            self.check_in_date_start = m.get('CheckInDateStart')

        if m.get('ChildCount') is not None:
            self.child_count = m.get('ChildCount')

        if m.get('ChildrenAges') is not None:
            self.children_ages = m.get('ChildrenAges')

        if m.get('RoomCount') is not None:
            self.room_count = m.get('RoomCount')

        if m.get('StandardHotelIds') is not None:
            self.standard_hotel_ids = m.get('StandardHotelIds')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

