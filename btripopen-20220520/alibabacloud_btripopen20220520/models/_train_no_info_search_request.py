# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TrainNoInfoSearchRequest(DaraModel):
    def __init__(
        self,
        arr_location: str = None,
        dep_date: str = None,
        dep_location: str = None,
        line_key: str = None,
        middle_date: str = None,
        middle_station: str = None,
        order_id: str = None,
        train_no: str = None,
    ):
        # This parameter is required.
        self.arr_location = arr_location
        # This parameter is required.
        self.dep_date = dep_date
        # This parameter is required.
        self.dep_location = dep_location
        self.line_key = line_key
        self.middle_date = middle_date
        self.middle_station = middle_station
        self.order_id = order_id
        self.train_no = train_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_location is not None:
            result['arr_location'] = self.arr_location

        if self.dep_date is not None:
            result['dep_date'] = self.dep_date

        if self.dep_location is not None:
            result['dep_location'] = self.dep_location

        if self.line_key is not None:
            result['line_key'] = self.line_key

        if self.middle_date is not None:
            result['middle_date'] = self.middle_date

        if self.middle_station is not None:
            result['middle_station'] = self.middle_station

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.train_no is not None:
            result['train_no'] = self.train_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_location') is not None:
            self.arr_location = m.get('arr_location')

        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')

        if m.get('dep_location') is not None:
            self.dep_location = m.get('dep_location')

        if m.get('line_key') is not None:
            self.line_key = m.get('line_key')

        if m.get('middle_date') is not None:
            self.middle_date = m.get('middle_date')

        if m.get('middle_station') is not None:
            self.middle_station = m.get('middle_station')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('train_no') is not None:
            self.train_no = m.get('train_no')

        return self

