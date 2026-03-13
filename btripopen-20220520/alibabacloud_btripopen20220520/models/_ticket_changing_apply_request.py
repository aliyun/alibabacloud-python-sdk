# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TicketChangingApplyRequest(DaraModel):
    def __init__(
        self,
        dis_order_id: str = None,
        dis_sub_order_id: str = None,
        is_voluntary: int = None,
        modify_flight_info_list: List[main_models.TicketChangingApplyRequestModifyFlightInfoList] = None,
        ota_item_id: str = None,
        reason: str = None,
        session_id: str = None,
        whether_retry: bool = None,
    ):
        # This parameter is required.
        self.dis_order_id = dis_order_id
        # This parameter is required.
        self.dis_sub_order_id = dis_sub_order_id
        self.is_voluntary = is_voluntary
        # This parameter is required.
        self.modify_flight_info_list = modify_flight_info_list
        # This parameter is required.
        self.ota_item_id = ota_item_id
        self.reason = reason
        # This parameter is required.
        self.session_id = session_id
        self.whether_retry = whether_retry

    def validate(self):
        if self.modify_flight_info_list:
            for v1 in self.modify_flight_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dis_order_id is not None:
            result['dis_order_id'] = self.dis_order_id

        if self.dis_sub_order_id is not None:
            result['dis_sub_order_id'] = self.dis_sub_order_id

        if self.is_voluntary is not None:
            result['is_voluntary'] = self.is_voluntary

        result['modify_flight_info_list'] = []
        if self.modify_flight_info_list is not None:
            for k1 in self.modify_flight_info_list:
                result['modify_flight_info_list'].append(k1.to_map() if k1 else None)

        if self.ota_item_id is not None:
            result['ota_item_id'] = self.ota_item_id

        if self.reason is not None:
            result['reason'] = self.reason

        if self.session_id is not None:
            result['session_id'] = self.session_id

        if self.whether_retry is not None:
            result['whether_retry'] = self.whether_retry

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dis_order_id') is not None:
            self.dis_order_id = m.get('dis_order_id')

        if m.get('dis_sub_order_id') is not None:
            self.dis_sub_order_id = m.get('dis_sub_order_id')

        if m.get('is_voluntary') is not None:
            self.is_voluntary = m.get('is_voluntary')

        self.modify_flight_info_list = []
        if m.get('modify_flight_info_list') is not None:
            for k1 in m.get('modify_flight_info_list'):
                temp_model = main_models.TicketChangingApplyRequestModifyFlightInfoList()
                self.modify_flight_info_list.append(temp_model.from_map(k1))

        if m.get('ota_item_id') is not None:
            self.ota_item_id = m.get('ota_item_id')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')

        if m.get('whether_retry') is not None:
            self.whether_retry = m.get('whether_retry')

        return self

class TicketChangingApplyRequestModifyFlightInfoList(DaraModel):
    def __init__(
        self,
        arr_city: str = None,
        cabin: str = None,
        dep_city: str = None,
        dep_date: str = None,
        flight_no: str = None,
        passenger_info_list: List[main_models.TicketChangingApplyRequestModifyFlightInfoListPassengerInfoList] = None,
    ):
        # This parameter is required.
        self.arr_city = arr_city
        self.cabin = cabin
        # This parameter is required.
        self.dep_city = dep_city
        # This parameter is required.
        self.dep_date = dep_date
        # This parameter is required.
        self.flight_no = flight_no
        # This parameter is required.
        self.passenger_info_list = passenger_info_list

    def validate(self):
        if self.passenger_info_list:
            for v1 in self.passenger_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_city is not None:
            result['arr_city'] = self.arr_city

        if self.cabin is not None:
            result['cabin'] = self.cabin

        if self.dep_city is not None:
            result['dep_city'] = self.dep_city

        if self.dep_date is not None:
            result['dep_date'] = self.dep_date

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        result['passenger_info_list'] = []
        if self.passenger_info_list is not None:
            for k1 in self.passenger_info_list:
                result['passenger_info_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        self.passenger_info_list = []
        if m.get('passenger_info_list') is not None:
            for k1 in m.get('passenger_info_list'):
                temp_model = main_models.TicketChangingApplyRequestModifyFlightInfoListPassengerInfoList()
                self.passenger_info_list.append(temp_model.from_map(k1))

        return self

class TicketChangingApplyRequestModifyFlightInfoListPassengerInfoList(DaraModel):
    def __init__(
        self,
        origin_flight_no: str = None,
        out_user_id: str = None,
        passenger_name: str = None,
    ):
        # This parameter is required.
        self.origin_flight_no = origin_flight_no
        # This parameter is required.
        self.out_user_id = out_user_id
        # This parameter is required.
        self.passenger_name = passenger_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.origin_flight_no is not None:
            result['origin_flight_no'] = self.origin_flight_no

        if self.out_user_id is not None:
            result['out_user_id'] = self.out_user_id

        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('origin_flight_no') is not None:
            self.origin_flight_no = m.get('origin_flight_no')

        if m.get('out_user_id') is not None:
            self.out_user_id = m.get('out_user_id')

        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')

        return self

