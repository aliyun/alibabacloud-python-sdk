# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TicketChangingFlightListRequest(DaraModel):
    def __init__(
        self,
        arr_city: str = None,
        dep_city: str = None,
        dep_date: str = None,
        dis_order_id: str = None,
        is_voluntary: int = None,
        traveler_info_list: List[main_models.TicketChangingFlightListRequestTravelerInfoList] = None,
    ):
        self.arr_city = arr_city
        self.dep_city = dep_city
        # This parameter is required.
        self.dep_date = dep_date
        # This parameter is required.
        self.dis_order_id = dis_order_id
        self.is_voluntary = is_voluntary
        self.traveler_info_list = traveler_info_list

    def validate(self):
        if self.traveler_info_list:
            for v1 in self.traveler_info_list:
                 if v1:
                    v1.validate()

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

        result['traveler_info_list'] = []
        if self.traveler_info_list is not None:
            for k1 in self.traveler_info_list:
                result['traveler_info_list'].append(k1.to_map() if k1 else None)

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

        self.traveler_info_list = []
        if m.get('traveler_info_list') is not None:
            for k1 in m.get('traveler_info_list'):
                temp_model = main_models.TicketChangingFlightListRequestTravelerInfoList()
                self.traveler_info_list.append(temp_model.from_map(k1))

        return self

class TicketChangingFlightListRequestTravelerInfoList(DaraModel):
    def __init__(
        self,
        arr_city: str = None,
        dep_city: str = None,
        name: str = None,
        type: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.arr_city = arr_city
        # This parameter is required.
        self.dep_city = dep_city
        self.name = name
        self.type = type
        # This parameter is required.
        self.user_id = user_id

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

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

