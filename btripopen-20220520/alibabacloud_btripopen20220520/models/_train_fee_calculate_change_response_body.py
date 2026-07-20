# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TrainFeeCalculateChangeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.TrainFeeCalculateChangeResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        # module
        self.module = module
        self.request_id = request_id
        self.success = success
        # traceId
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.module is not None:
            result['module'] = self.module.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('module') is not None:
            temp_model = main_models.TrainFeeCalculateChangeResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class TrainFeeCalculateChangeResponseBodyModule(DaraModel):
    def __init__(
        self,
        change_train_details: List[main_models.TrainFeeCalculateChangeResponseBodyModuleChangeTrainDetails] = None,
        distribute_order_id: str = None,
        order_id: str = None,
    ):
        self.change_train_details = change_train_details
        self.distribute_order_id = distribute_order_id
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
                temp_model = main_models.TrainFeeCalculateChangeResponseBodyModuleChangeTrainDetails()
                self.change_train_details.append(temp_model.from_map(k1))

        if m.get('distribute_order_id') is not None:
            self.distribute_order_id = m.get('distribute_order_id')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        return self

class TrainFeeCalculateChangeResponseBodyModuleChangeTrainDetails(DaraModel):
    def __init__(
        self,
        arr_station_code: str = None,
        change_ticket_details: List[main_models.TrainFeeCalculateChangeResponseBodyModuleChangeTrainDetailsChangeTicketDetails] = None,
        dep_station_code: str = None,
        dep_time: str = None,
        train_no: str = None,
    ):
        self.arr_station_code = arr_station_code
        self.change_ticket_details = change_ticket_details
        self.dep_station_code = dep_station_code
        self.dep_time = dep_time
        self.train_no = train_no

    def validate(self):
        if self.change_ticket_details:
            for v1 in self.change_ticket_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_station_code is not None:
            result['arr_station_code'] = self.arr_station_code

        result['change_ticket_details'] = []
        if self.change_ticket_details is not None:
            for k1 in self.change_ticket_details:
                result['change_ticket_details'].append(k1.to_map() if k1 else None)

        if self.dep_station_code is not None:
            result['dep_station_code'] = self.dep_station_code

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.train_no is not None:
            result['train_no'] = self.train_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_station_code') is not None:
            self.arr_station_code = m.get('arr_station_code')

        self.change_ticket_details = []
        if m.get('change_ticket_details') is not None:
            for k1 in m.get('change_ticket_details'):
                temp_model = main_models.TrainFeeCalculateChangeResponseBodyModuleChangeTrainDetailsChangeTicketDetails()
                self.change_ticket_details.append(temp_model.from_map(k1))

        if m.get('dep_station_code') is not None:
            self.dep_station_code = m.get('dep_station_code')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('train_no') is not None:
            self.train_no = m.get('train_no')

        return self

class TrainFeeCalculateChangeResponseBodyModuleChangeTrainDetailsChangeTicketDetails(DaraModel):
    def __init__(
        self,
        change_fee: int = None,
        change_rate: int = None,
        change_refund_fee: int = None,
        change_refund_rate: int = None,
        passenger_info: main_models.TrainFeeCalculateChangeResponseBodyModuleChangeTrainDetailsChangeTicketDetailsPassengerInfo = None,
        seat_type: str = None,
        ticket_price: int = None,
    ):
        self.change_fee = change_fee
        self.change_rate = change_rate
        self.change_refund_fee = change_refund_fee
        self.change_refund_rate = change_refund_rate
        self.passenger_info = passenger_info
        self.seat_type = seat_type
        self.ticket_price = ticket_price

    def validate(self):
        if self.passenger_info:
            self.passenger_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_fee is not None:
            result['change_fee'] = self.change_fee

        if self.change_rate is not None:
            result['change_rate'] = self.change_rate

        if self.change_refund_fee is not None:
            result['change_refund_fee'] = self.change_refund_fee

        if self.change_refund_rate is not None:
            result['change_refund_rate'] = self.change_refund_rate

        if self.passenger_info is not None:
            result['passenger_info'] = self.passenger_info.to_map()

        if self.seat_type is not None:
            result['seat_type'] = self.seat_type

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('change_fee') is not None:
            self.change_fee = m.get('change_fee')

        if m.get('change_rate') is not None:
            self.change_rate = m.get('change_rate')

        if m.get('change_refund_fee') is not None:
            self.change_refund_fee = m.get('change_refund_fee')

        if m.get('change_refund_rate') is not None:
            self.change_refund_rate = m.get('change_refund_rate')

        if m.get('passenger_info') is not None:
            temp_model = main_models.TrainFeeCalculateChangeResponseBodyModuleChangeTrainDetailsChangeTicketDetailsPassengerInfo()
            self.passenger_info = temp_model.from_map(m.get('passenger_info'))

        if m.get('seat_type') is not None:
            self.seat_type = m.get('seat_type')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        return self

class TrainFeeCalculateChangeResponseBodyModuleChangeTrainDetailsChangeTicketDetailsPassengerInfo(DaraModel):
    def __init__(
        self,
        passenger_cert_no: str = None,
        passenger_cert_type: str = None,
        passenger_id: str = None,
        passenger_name: str = None,
    ):
        self.passenger_cert_no = passenger_cert_no
        self.passenger_cert_type = passenger_cert_type
        self.passenger_id = passenger_id
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

        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passenger_cert_no') is not None:
            self.passenger_cert_no = m.get('passenger_cert_no')

        if m.get('passenger_cert_type') is not None:
            self.passenger_cert_type = m.get('passenger_cert_type')

        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')

        return self

