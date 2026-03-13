# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TrainStopoverSearchRequest(DaraModel):
    def __init__(
        self,
        arr_station: str = None,
        dep_station: str = None,
        train_date: str = None,
        train_no: str = None,
    ):
        # This parameter is required.
        self.arr_station = arr_station
        # This parameter is required.
        self.dep_station = dep_station
        # This parameter is required.
        self.train_date = train_date
        # This parameter is required.
        self.train_no = train_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_station is not None:
            result['arr_station'] = self.arr_station

        if self.dep_station is not None:
            result['dep_station'] = self.dep_station

        if self.train_date is not None:
            result['train_date'] = self.train_date

        if self.train_no is not None:
            result['train_no'] = self.train_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_station') is not None:
            self.arr_station = m.get('arr_station')

        if m.get('dep_station') is not None:
            self.dep_station = m.get('dep_station')

        if m.get('train_date') is not None:
            self.train_date = m.get('train_date')

        if m.get('train_no') is not None:
            self.train_no = m.get('train_no')

        return self

