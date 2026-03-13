# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TicketChangingEnquiryRequest(DaraModel):
    def __init__(
        self,
        arr_city: str = None,
        dep_city: str = None,
        dis_order_id: str = None,
        is_voluntary: int = None,
        modify_depart_date: str = None,
        modify_flight_no: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.arr_city = arr_city
        # This parameter is required.
        self.dep_city = dep_city
        # This parameter is required.
        self.dis_order_id = dis_order_id
        # This parameter is required.
        self.is_voluntary = is_voluntary
        # This parameter is required.
        self.modify_depart_date = modify_depart_date
        # This parameter is required.
        self.modify_flight_no = modify_flight_no
        # This parameter is required.
        self.session_id = session_id

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

        if self.dis_order_id is not None:
            result['dis_order_id'] = self.dis_order_id

        if self.is_voluntary is not None:
            result['is_voluntary'] = self.is_voluntary

        if self.modify_depart_date is not None:
            result['modify_depart_date'] = self.modify_depart_date

        if self.modify_flight_no is not None:
            result['modify_flight_no'] = self.modify_flight_no

        if self.session_id is not None:
            result['session_id'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('dis_order_id') is not None:
            self.dis_order_id = m.get('dis_order_id')

        if m.get('is_voluntary') is not None:
            self.is_voluntary = m.get('is_voluntary')

        if m.get('modify_depart_date') is not None:
            self.modify_depart_date = m.get('modify_depart_date')

        if m.get('modify_flight_no') is not None:
            self.modify_flight_no = m.get('modify_flight_no')

        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')

        return self

