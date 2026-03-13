# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TrainFeeCalculateRefundResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.TrainFeeCalculateRefundResponseBodyModule = None,
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
            temp_model = main_models.TrainFeeCalculateRefundResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class TrainFeeCalculateRefundResponseBodyModule(DaraModel):
    def __init__(
        self,
        distribute_order_id: str = None,
        order_id: str = None,
        refund_train_details: List[main_models.TrainFeeCalculateRefundResponseBodyModuleRefundTrainDetails] = None,
    ):
        self.distribute_order_id = distribute_order_id
        self.order_id = order_id
        self.refund_train_details = refund_train_details

    def validate(self):
        if self.refund_train_details:
            for v1 in self.refund_train_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.distribute_order_id is not None:
            result['distribute_order_id'] = self.distribute_order_id

        if self.order_id is not None:
            result['order_id'] = self.order_id

        result['refund_train_details'] = []
        if self.refund_train_details is not None:
            for k1 in self.refund_train_details:
                result['refund_train_details'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('distribute_order_id') is not None:
            self.distribute_order_id = m.get('distribute_order_id')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        self.refund_train_details = []
        if m.get('refund_train_details') is not None:
            for k1 in m.get('refund_train_details'):
                temp_model = main_models.TrainFeeCalculateRefundResponseBodyModuleRefundTrainDetails()
                self.refund_train_details.append(temp_model.from_map(k1))

        return self

class TrainFeeCalculateRefundResponseBodyModuleRefundTrainDetails(DaraModel):
    def __init__(
        self,
        arr_station_code: str = None,
        dep_station_code: str = None,
        dep_time: str = None,
        refund_ticket_details: List[main_models.TrainFeeCalculateRefundResponseBodyModuleRefundTrainDetailsRefundTicketDetails] = None,
        train_no: str = None,
    ):
        self.arr_station_code = arr_station_code
        self.dep_station_code = dep_station_code
        self.dep_time = dep_time
        self.refund_ticket_details = refund_ticket_details
        self.train_no = train_no

    def validate(self):
        if self.refund_ticket_details:
            for v1 in self.refund_ticket_details:
                 if v1:
                    v1.validate()

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

        result['refund_ticket_details'] = []
        if self.refund_ticket_details is not None:
            for k1 in self.refund_ticket_details:
                result['refund_ticket_details'].append(k1.to_map() if k1 else None)

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

        self.refund_ticket_details = []
        if m.get('refund_ticket_details') is not None:
            for k1 in m.get('refund_ticket_details'):
                temp_model = main_models.TrainFeeCalculateRefundResponseBodyModuleRefundTrainDetailsRefundTicketDetails()
                self.refund_ticket_details.append(temp_model.from_map(k1))

        if m.get('train_no') is not None:
            self.train_no = m.get('train_no')

        return self

class TrainFeeCalculateRefundResponseBodyModuleRefundTrainDetailsRefundTicketDetails(DaraModel):
    def __init__(
        self,
        can_refund: bool = None,
        passenger_info: main_models.TrainFeeCalculateRefundResponseBodyModuleRefundTrainDetailsRefundTicketDetailsPassengerInfo = None,
        refund_cost_fee: int = None,
        refund_price: int = None,
        refund_rate: int = None,
        ticket_price: int = None,
    ):
        self.can_refund = can_refund
        self.passenger_info = passenger_info
        self.refund_cost_fee = refund_cost_fee
        self.refund_price = refund_price
        self.refund_rate = refund_rate
        self.ticket_price = ticket_price

    def validate(self):
        if self.passenger_info:
            self.passenger_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_refund is not None:
            result['can_refund'] = self.can_refund

        if self.passenger_info is not None:
            result['passenger_info'] = self.passenger_info.to_map()

        if self.refund_cost_fee is not None:
            result['refund_cost_fee'] = self.refund_cost_fee

        if self.refund_price is not None:
            result['refund_price'] = self.refund_price

        if self.refund_rate is not None:
            result['refund_rate'] = self.refund_rate

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('can_refund') is not None:
            self.can_refund = m.get('can_refund')

        if m.get('passenger_info') is not None:
            temp_model = main_models.TrainFeeCalculateRefundResponseBodyModuleRefundTrainDetailsRefundTicketDetailsPassengerInfo()
            self.passenger_info = temp_model.from_map(m.get('passenger_info'))

        if m.get('refund_cost_fee') is not None:
            self.refund_cost_fee = m.get('refund_cost_fee')

        if m.get('refund_price') is not None:
            self.refund_price = m.get('refund_price')

        if m.get('refund_rate') is not None:
            self.refund_rate = m.get('refund_rate')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        return self

class TrainFeeCalculateRefundResponseBodyModuleRefundTrainDetailsRefundTicketDetailsPassengerInfo(DaraModel):
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

