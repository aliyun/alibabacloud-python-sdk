# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetSubscriptionSeatDetailsRequest(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        query_assigned: bool = None,
        seat_id: str = None,
        seat_type: str = None,
        status_list: List[str] = None,
    ):
        # The page number. Default value: 1. Valid values: positive integers.
        self.page_no = page_no
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The seat assignment status filter. Set to true for assigned seats, false for unassigned seats, or null for all seats.
        self.query_assigned = query_assigned
        # The seat ID.
        self.seat_id = seat_id
        # The seat type (specType). Valid values:
        # 
        # - standard: standard seat.
        # - pro: pro seat.
        # - max: premium seat.
        self.seat_type = seat_type
        # The list of seat statuses used for filtering.
        self.status_list = status_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_assigned is not None:
            result['QueryAssigned'] = self.query_assigned

        if self.seat_id is not None:
            result['SeatId'] = self.seat_id

        if self.seat_type is not None:
            result['SeatType'] = self.seat_type

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryAssigned') is not None:
            self.query_assigned = m.get('QueryAssigned')

        if m.get('SeatId') is not None:
            self.seat_id = m.get('SeatId')

        if m.get('SeatType') is not None:
            self.seat_type = m.get('SeatType')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        return self

