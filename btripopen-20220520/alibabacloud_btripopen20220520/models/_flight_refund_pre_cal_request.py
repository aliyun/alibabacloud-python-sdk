# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightRefundPreCalRequest(DaraModel):
    def __init__(
        self,
        dis_order_id: str = None,
        is_voluntary: str = None,
        passenger_segment_info_list: List[main_models.FlightRefundPreCalRequestPassengerSegmentInfoList] = None,
    ):
        # This parameter is required.
        self.dis_order_id = dis_order_id
        self.is_voluntary = is_voluntary
        # This parameter is required.
        self.passenger_segment_info_list = passenger_segment_info_list

    def validate(self):
        if self.passenger_segment_info_list:
            for v1 in self.passenger_segment_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dis_order_id is not None:
            result['dis_order_id'] = self.dis_order_id

        if self.is_voluntary is not None:
            result['is_voluntary'] = self.is_voluntary

        result['passenger_segment_info_list'] = []
        if self.passenger_segment_info_list is not None:
            for k1 in self.passenger_segment_info_list:
                result['passenger_segment_info_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dis_order_id') is not None:
            self.dis_order_id = m.get('dis_order_id')

        if m.get('is_voluntary') is not None:
            self.is_voluntary = m.get('is_voluntary')

        self.passenger_segment_info_list = []
        if m.get('passenger_segment_info_list') is not None:
            for k1 in m.get('passenger_segment_info_list'):
                temp_model = main_models.FlightRefundPreCalRequestPassengerSegmentInfoList()
                self.passenger_segment_info_list.append(temp_model.from_map(k1))

        return self

class FlightRefundPreCalRequestPassengerSegmentInfoList(DaraModel):
    def __init__(
        self,
        flight_no: str = None,
        passenger_name: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.flight_no = flight_no
        # This parameter is required.
        self.passenger_name = passenger_name
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

