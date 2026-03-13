# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TicketChangingDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.TicketChangingDetailResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.request_id = request_id
        self.success = success
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
            temp_model = main_models.TicketChangingDetailResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class TicketChangingDetailResponseBodyModule(DaraModel):
    def __init__(
        self,
        alipay_trade_no: str = None,
        btrip_order_id: int = None,
        btrip_sub_order_id: int = None,
        dis_order_id: str = None,
        dis_sub_order_id: str = None,
        extra: str = None,
        flight_info_list: List[main_models.TicketChangingDetailResponseBodyModuleFlightInfoList] = None,
        last_pay_time: str = None,
        pay_status: int = None,
        pay_time: str = None,
        settle_price: int = None,
        settle_type: int = None,
        status: int = None,
        total_change_price: int = None,
        total_price: int = None,
        total_upgrade_price: int = None,
        traveler_info_list: List[main_models.TicketChangingDetailResponseBodyModuleTravelerInfoList] = None,
    ):
        self.alipay_trade_no = alipay_trade_no
        self.btrip_order_id = btrip_order_id
        self.btrip_sub_order_id = btrip_sub_order_id
        self.dis_order_id = dis_order_id
        self.dis_sub_order_id = dis_sub_order_id
        self.extra = extra
        self.flight_info_list = flight_info_list
        self.last_pay_time = last_pay_time
        self.pay_status = pay_status
        self.pay_time = pay_time
        self.settle_price = settle_price
        self.settle_type = settle_type
        self.status = status
        self.total_change_price = total_change_price
        self.total_price = total_price
        self.total_upgrade_price = total_upgrade_price
        self.traveler_info_list = traveler_info_list

    def validate(self):
        if self.flight_info_list:
            for v1 in self.flight_info_list:
                 if v1:
                    v1.validate()
        if self.traveler_info_list:
            for v1 in self.traveler_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alipay_trade_no is not None:
            result['alipay_trade_no'] = self.alipay_trade_no

        if self.btrip_order_id is not None:
            result['btrip_order_id'] = self.btrip_order_id

        if self.btrip_sub_order_id is not None:
            result['btrip_sub_order_id'] = self.btrip_sub_order_id

        if self.dis_order_id is not None:
            result['dis_order_id'] = self.dis_order_id

        if self.dis_sub_order_id is not None:
            result['dis_sub_order_id'] = self.dis_sub_order_id

        if self.extra is not None:
            result['extra'] = self.extra

        result['flight_info_list'] = []
        if self.flight_info_list is not None:
            for k1 in self.flight_info_list:
                result['flight_info_list'].append(k1.to_map() if k1 else None)

        if self.last_pay_time is not None:
            result['last_pay_time'] = self.last_pay_time

        if self.pay_status is not None:
            result['pay_status'] = self.pay_status

        if self.pay_time is not None:
            result['pay_time'] = self.pay_time

        if self.settle_price is not None:
            result['settle_price'] = self.settle_price

        if self.settle_type is not None:
            result['settle_type'] = self.settle_type

        if self.status is not None:
            result['status'] = self.status

        if self.total_change_price is not None:
            result['total_change_price'] = self.total_change_price

        if self.total_price is not None:
            result['total_price'] = self.total_price

        if self.total_upgrade_price is not None:
            result['total_upgrade_price'] = self.total_upgrade_price

        result['traveler_info_list'] = []
        if self.traveler_info_list is not None:
            for k1 in self.traveler_info_list:
                result['traveler_info_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alipay_trade_no') is not None:
            self.alipay_trade_no = m.get('alipay_trade_no')

        if m.get('btrip_order_id') is not None:
            self.btrip_order_id = m.get('btrip_order_id')

        if m.get('btrip_sub_order_id') is not None:
            self.btrip_sub_order_id = m.get('btrip_sub_order_id')

        if m.get('dis_order_id') is not None:
            self.dis_order_id = m.get('dis_order_id')

        if m.get('dis_sub_order_id') is not None:
            self.dis_sub_order_id = m.get('dis_sub_order_id')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        self.flight_info_list = []
        if m.get('flight_info_list') is not None:
            for k1 in m.get('flight_info_list'):
                temp_model = main_models.TicketChangingDetailResponseBodyModuleFlightInfoList()
                self.flight_info_list.append(temp_model.from_map(k1))

        if m.get('last_pay_time') is not None:
            self.last_pay_time = m.get('last_pay_time')

        if m.get('pay_status') is not None:
            self.pay_status = m.get('pay_status')

        if m.get('pay_time') is not None:
            self.pay_time = m.get('pay_time')

        if m.get('settle_price') is not None:
            self.settle_price = m.get('settle_price')

        if m.get('settle_type') is not None:
            self.settle_type = m.get('settle_type')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('total_change_price') is not None:
            self.total_change_price = m.get('total_change_price')

        if m.get('total_price') is not None:
            self.total_price = m.get('total_price')

        if m.get('total_upgrade_price') is not None:
            self.total_upgrade_price = m.get('total_upgrade_price')

        self.traveler_info_list = []
        if m.get('traveler_info_list') is not None:
            for k1 in m.get('traveler_info_list'):
                temp_model = main_models.TicketChangingDetailResponseBodyModuleTravelerInfoList()
                self.traveler_info_list.append(temp_model.from_map(k1))

        return self

class TicketChangingDetailResponseBodyModuleTravelerInfoList(DaraModel):
    def __init__(
        self,
        birth_date: str = None,
        cert_no: str = None,
        cert_type: str = None,
        open_ticket_status: int = None,
        passenger_name: str = None,
        passenger_type: str = None,
        phone: str = None,
        ticket_no: str = None,
        user_id: str = None,
    ):
        self.birth_date = birth_date
        self.cert_no = cert_no
        self.cert_type = cert_type
        self.open_ticket_status = open_ticket_status
        self.passenger_name = passenger_name
        self.passenger_type = passenger_type
        self.phone = phone
        self.ticket_no = ticket_no
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.birth_date is not None:
            result['birth_date'] = self.birth_date

        if self.cert_no is not None:
            result['cert_no'] = self.cert_no

        if self.cert_type is not None:
            result['cert_type'] = self.cert_type

        if self.open_ticket_status is not None:
            result['open_ticket_status'] = self.open_ticket_status

        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name

        if self.passenger_type is not None:
            result['passenger_type'] = self.passenger_type

        if self.phone is not None:
            result['phone'] = self.phone

        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('birth_date') is not None:
            self.birth_date = m.get('birth_date')

        if m.get('cert_no') is not None:
            self.cert_no = m.get('cert_no')

        if m.get('cert_type') is not None:
            self.cert_type = m.get('cert_type')

        if m.get('open_ticket_status') is not None:
            self.open_ticket_status = m.get('open_ticket_status')

        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')

        if m.get('passenger_type') is not None:
            self.passenger_type = m.get('passenger_type')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class TicketChangingDetailResponseBodyModuleFlightInfoList(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        airline_name: str = None,
        airline_simple_name: str = None,
        arr_airport: str = None,
        arr_airport_code: str = None,
        arr_airport_code_name: str = None,
        arr_city: str = None,
        arr_city_code: str = None,
        arr_terminal: str = None,
        arr_time: str = None,
        baggage: str = None,
        build_price: int = None,
        cabin: str = None,
        cabin_class: str = None,
        carrier: str = None,
        dep_airport: str = None,
        dep_airport_code: str = None,
        dep_airport_code_name: str = None,
        dep_city: str = None,
        dep_city_code: str = None,
        dep_terminal: str = None,
        dep_time: str = None,
        flight_no: str = None,
        last_cabin: str = None,
        last_flight_no: str = None,
        meal: str = None,
        oil_price: int = None,
        segment_type: int = None,
        stop_arr_time: str = None,
        stop_city: str = None,
        stop_dep_time: str = None,
        ticket_price: int = None,
        tuigaiqian_info: str = None,
    ):
        self.airline_code = airline_code
        self.airline_name = airline_name
        self.airline_simple_name = airline_simple_name
        self.arr_airport = arr_airport
        self.arr_airport_code = arr_airport_code
        self.arr_airport_code_name = arr_airport_code_name
        self.arr_city = arr_city
        self.arr_city_code = arr_city_code
        self.arr_terminal = arr_terminal
        self.arr_time = arr_time
        self.baggage = baggage
        self.build_price = build_price
        self.cabin = cabin
        self.cabin_class = cabin_class
        self.carrier = carrier
        self.dep_airport = dep_airport
        self.dep_airport_code = dep_airport_code
        self.dep_airport_code_name = dep_airport_code_name
        self.dep_city = dep_city
        self.dep_city_code = dep_city_code
        self.dep_terminal = dep_terminal
        self.dep_time = dep_time
        self.flight_no = flight_no
        self.last_cabin = last_cabin
        self.last_flight_no = last_flight_no
        self.meal = meal
        self.oil_price = oil_price
        self.segment_type = segment_type
        self.stop_arr_time = stop_arr_time
        self.stop_city = stop_city
        self.stop_dep_time = stop_dep_time
        self.ticket_price = ticket_price
        self.tuigaiqian_info = tuigaiqian_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_code is not None:
            result['airline_code'] = self.airline_code

        if self.airline_name is not None:
            result['airline_name'] = self.airline_name

        if self.airline_simple_name is not None:
            result['airline_simple_name'] = self.airline_simple_name

        if self.arr_airport is not None:
            result['arr_airport'] = self.arr_airport

        if self.arr_airport_code is not None:
            result['arr_airport_code'] = self.arr_airport_code

        if self.arr_airport_code_name is not None:
            result['arr_airport_code_name'] = self.arr_airport_code_name

        if self.arr_city is not None:
            result['arr_city'] = self.arr_city

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_terminal is not None:
            result['arr_terminal'] = self.arr_terminal

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.baggage is not None:
            result['baggage'] = self.baggage

        if self.build_price is not None:
            result['build_price'] = self.build_price

        if self.cabin is not None:
            result['cabin'] = self.cabin

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.carrier is not None:
            result['carrier'] = self.carrier

        if self.dep_airport is not None:
            result['dep_airport'] = self.dep_airport

        if self.dep_airport_code is not None:
            result['dep_airport_code'] = self.dep_airport_code

        if self.dep_airport_code_name is not None:
            result['dep_airport_code_name'] = self.dep_airport_code_name

        if self.dep_city is not None:
            result['dep_city'] = self.dep_city

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_terminal is not None:
            result['dep_terminal'] = self.dep_terminal

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.last_cabin is not None:
            result['last_cabin'] = self.last_cabin

        if self.last_flight_no is not None:
            result['last_flight_no'] = self.last_flight_no

        if self.meal is not None:
            result['meal'] = self.meal

        if self.oil_price is not None:
            result['oil_price'] = self.oil_price

        if self.segment_type is not None:
            result['segment_type'] = self.segment_type

        if self.stop_arr_time is not None:
            result['stop_arr_time'] = self.stop_arr_time

        if self.stop_city is not None:
            result['stop_city'] = self.stop_city

        if self.stop_dep_time is not None:
            result['stop_dep_time'] = self.stop_dep_time

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        if self.tuigaiqian_info is not None:
            result['tuigaiqian_info'] = self.tuigaiqian_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_name') is not None:
            self.airline_name = m.get('airline_name')

        if m.get('airline_simple_name') is not None:
            self.airline_simple_name = m.get('airline_simple_name')

        if m.get('arr_airport') is not None:
            self.arr_airport = m.get('arr_airport')

        if m.get('arr_airport_code') is not None:
            self.arr_airport_code = m.get('arr_airport_code')

        if m.get('arr_airport_code_name') is not None:
            self.arr_airport_code_name = m.get('arr_airport_code_name')

        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_terminal') is not None:
            self.arr_terminal = m.get('arr_terminal')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('baggage') is not None:
            self.baggage = m.get('baggage')

        if m.get('build_price') is not None:
            self.build_price = m.get('build_price')

        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('carrier') is not None:
            self.carrier = m.get('carrier')

        if m.get('dep_airport') is not None:
            self.dep_airport = m.get('dep_airport')

        if m.get('dep_airport_code') is not None:
            self.dep_airport_code = m.get('dep_airport_code')

        if m.get('dep_airport_code_name') is not None:
            self.dep_airport_code_name = m.get('dep_airport_code_name')

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_terminal') is not None:
            self.dep_terminal = m.get('dep_terminal')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('last_cabin') is not None:
            self.last_cabin = m.get('last_cabin')

        if m.get('last_flight_no') is not None:
            self.last_flight_no = m.get('last_flight_no')

        if m.get('meal') is not None:
            self.meal = m.get('meal')

        if m.get('oil_price') is not None:
            self.oil_price = m.get('oil_price')

        if m.get('segment_type') is not None:
            self.segment_type = m.get('segment_type')

        if m.get('stop_arr_time') is not None:
            self.stop_arr_time = m.get('stop_arr_time')

        if m.get('stop_city') is not None:
            self.stop_city = m.get('stop_city')

        if m.get('stop_dep_time') is not None:
            self.stop_dep_time = m.get('stop_dep_time')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        if m.get('tuigaiqian_info') is not None:
            self.tuigaiqian_info = m.get('tuigaiqian_info')

        return self

