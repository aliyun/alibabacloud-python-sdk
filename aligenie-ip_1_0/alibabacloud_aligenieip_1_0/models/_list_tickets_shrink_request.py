# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTicketsShrinkRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        hotel_id: str = None,
        is_desc: bool = None,
        is_need_callback: bool = None,
        is_need_charges: bool = None,
        page_shrink: str = None,
        room_no: str = None,
        sort_field: str = None,
        start_time: str = None,
        status: str = None,
        type: str = None,
    ):
        self.end_time = end_time
        # This parameter is required.
        self.hotel_id = hotel_id
        self.is_desc = is_desc
        self.is_need_callback = is_need_callback
        self.is_need_charges = is_need_charges
        self.page_shrink = page_shrink
        self.room_no = room_no
        self.sort_field = sort_field
        self.start_time = start_time
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.is_desc is not None:
            result['IsDesc'] = self.is_desc

        if self.is_need_callback is not None:
            result['IsNeedCallback'] = self.is_need_callback

        if self.is_need_charges is not None:
            result['IsNeedCharges'] = self.is_need_charges

        if self.page_shrink is not None:
            result['Page'] = self.page_shrink

        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        if self.sort_field is not None:
            result['SortField'] = self.sort_field

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('IsDesc') is not None:
            self.is_desc = m.get('IsDesc')

        if m.get('IsNeedCallback') is not None:
            self.is_need_callback = m.get('IsNeedCallback')

        if m.get('IsNeedCharges') is not None:
            self.is_need_charges = m.get('IsNeedCharges')

        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')

        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

