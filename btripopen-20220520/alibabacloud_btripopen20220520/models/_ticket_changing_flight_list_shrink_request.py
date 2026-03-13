# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TicketChangingFlightListShrinkRequest(DaraModel):
    def __init__(
        self,
        arr_city: str = None,
        dep_city: str = None,
        dep_date: str = None,
        dis_order_id: str = None,
        is_voluntary: int = None,
        traveler_info_list_shrink: str = None,
    ):
        self.arr_city = arr_city
        self.dep_city = dep_city
        # This parameter is required.
        self.dep_date = dep_date
        # This parameter is required.
        self.dis_order_id = dis_order_id
        self.is_voluntary = is_voluntary
        self.traveler_info_list_shrink = traveler_info_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_city is not None:
            result['arr_city'] = self.arr_city

        if self.dep_city is not None:
            result['dep_city'] = self.dep_city

        if self.dep_date is not None:
            result['dep_date'] = self.dep_date

        if self.dis_order_id is not None:
            result['dis_order_id'] = self.dis_order_id

        if self.is_voluntary is not None:
            result['is_voluntary'] = self.is_voluntary

        if self.traveler_info_list_shrink is not None:
            result['traveler_info_list'] = self.traveler_info_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')

        if m.get('dis_order_id') is not None:
            self.dis_order_id = m.get('dis_order_id')

        if m.get('is_voluntary') is not None:
            self.is_voluntary = m.get('is_voluntary')

        if m.get('traveler_info_list') is not None:
            self.traveler_info_list_shrink = m.get('traveler_info_list')

        return self

