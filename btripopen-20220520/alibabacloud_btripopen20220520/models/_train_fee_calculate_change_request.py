# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TrainFeeCalculateChangeRequest(DaraModel):
    def __init__(
        self,
        change_train_details: List[main_models.TrainFeeCalculateChangeRequestChangeTrainDetails] = None,
        distribute_order_id: str = None,
        order_id: str = None,
    ):
        # This parameter is required.
        self.change_train_details = change_train_details
        # This parameter is required.
        self.distribute_order_id = distribute_order_id
        # This parameter is required.
        self.order_id = order_id

    def validate(self):
        if self.change_train_details:
            for v1 in self.change_train_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['change_train_details'] = []
        if self.change_train_details is not None:
            for k1 in self.change_train_details:
                result['change_train_details'].append(k1.to_map() if k1 else None)

        if self.distribute_order_id is not None:
            result['distribute_order_id'] = self.distribute_order_id

        if self.order_id is not None:
            result['order_id'] = self.order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.change_train_details = []
        if m.get('change_train_details') is not None:
            for k1 in m.get('change_train_details'):
                temp_model = main_models.TrainFeeCalculateChangeRequestChangeTrainDetails()
                self.change_train_details.append(temp_model.from_map(k1))

        if m.get('distribute_order_id') is not None:
            self.distribute_order_id = m.get('distribute_order_id')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        return self

class TrainFeeCalculateChangeRequestChangeTrainDetails(DaraModel):
    def __init__(
        self,
        arr_station_code: str = None,
        dep_station_code: str = None,
        dep_time: str = None,
        original_dep_time: str = None,
        original_train_no: str = None,
        passenger_info: main_models.TrainFeeCalculateChangeRequestChangeTrainDetailsPassengerInfo = None,
        seat_type: str = None,
        train_no: str = None,
    ):
        # This parameter is required.
        self.arr_station_code = arr_station_code
        # This parameter is required.
        self.dep_station_code = dep_station_code
        # This parameter is required.
        self.dep_time = dep_time
        # This parameter is required.
        self.original_dep_time = original_dep_time
        # This parameter is required.
        self.original_train_no = original_train_no
        # This parameter is required.
        self.passenger_info = passenger_info
        # This parameter is required.
        self.seat_type = seat_type
        # This parameter is required.
        self.train_no = train_no

    def validate(self):
        if self.passenger_info:
            self.passenger_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_station_code is not None:
            result['arr_station_code'] = self.arr_station_code

        if self.dep_station_code is not None:
            result['dep_station_code'] = self.dep_station_code

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.original_dep_time is not None:
            result['original_dep_time'] = self.original_dep_time

        if self.original_train_no is not None:
            result['original_train_no'] = self.original_train_no

        if self.passenger_info is not None:
            result['passenger_info'] = self.passenger_info.to_map()

        if self.seat_type is not None:
            result['seat_type'] = self.seat_type

        if self.train_no is not None:
            result['train_no'] = self.train_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_station_code') is not None:
            self.arr_station_code = m.get('arr_station_code')

        if m.get('dep_station_code') is not None:
            self.dep_station_code = m.get('dep_station_code')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('original_dep_time') is not None:
            self.original_dep_time = m.get('original_dep_time')

        if m.get('original_train_no') is not None:
            self.original_train_no = m.get('original_train_no')

        if m.get('passenger_info') is not None:
            temp_model = main_models.TrainFeeCalculateChangeRequestChangeTrainDetailsPassengerInfo()
            self.passenger_info = temp_model.from_map(m.get('passenger_info'))

        if m.get('seat_type') is not None:
            self.seat_type = m.get('seat_type')

        if m.get('train_no') is not None:
            self.train_no = m.get('train_no')

        return self

class TrainFeeCalculateChangeRequestChangeTrainDetailsPassengerInfo(DaraModel):
    def __init__(
        self,
        passenger_cert_no: str = None,
        passenger_cert_type: str = None,
        passenger_name: str = None,
    ):
        # This parameter is required.
        self.passenger_cert_no = passenger_cert_no
        # This parameter is required.
        self.passenger_cert_type = passenger_cert_type
        # This parameter is required.
        self.passenger_name = passenger_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.passenger_cert_no is not None:
            result['passenger_cert_no'] = self.passenger_cert_no

        if self.passenger_cert_type is not None:
            result['passenger_cert_type'] = self.passenger_cert_type

        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passenger_cert_no') is not None:
            self.passenger_cert_no = m.get('passenger_cert_no')

        if m.get('passenger_cert_type') is not None:
            self.passenger_cert_type = m.get('passenger_cert_type')

        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')

        return self

