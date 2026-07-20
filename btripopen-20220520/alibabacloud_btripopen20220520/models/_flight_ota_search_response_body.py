# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightOtaSearchResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.FlightOtaSearchResponseBodyModule = None,
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
            temp_model = main_models.FlightOtaSearchResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class FlightOtaSearchResponseBodyModule(DaraModel):
    def __init__(
        self,
        flight_list: List[main_models.FlightOtaSearchResponseBodyModuleFlightList] = None,
    ):
        self.flight_list = flight_list

    def validate(self):
        if self.flight_list:
            for v1 in self.flight_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['flight_list'] = []
        if self.flight_list is not None:
            for k1 in self.flight_list:
                result['flight_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flight_list = []
        if m.get('flight_list') is not None:
            for k1 in m.get('flight_list'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightList()
                self.flight_list.append(temp_model.from_map(k1))

        return self

class FlightOtaSearchResponseBodyModuleFlightList(DaraModel):
    def __init__(
        self,
        airline_info: main_models.FlightOtaSearchResponseBodyModuleFlightListAirlineInfo = None,
        arr_airport_info: main_models.FlightOtaSearchResponseBodyModuleFlightListArrAirportInfo = None,
        arr_date: str = None,
        build_price: int = None,
        cabin: str = None,
        cabin_class: str = None,
        cabin_info_list: List[main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoList] = None,
        carrier_airline: str = None,
        carrier_no: str = None,
        dep_airport_info: main_models.FlightOtaSearchResponseBodyModuleFlightListDepAirportInfo = None,
        dep_city_code: str = None,
        dep_date: str = None,
        discount: int = None,
        flight_no: str = None,
        flight_rule_list: List[main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleList] = None,
        flight_rule_list_str: str = None,
        flight_size: str = None,
        flight_type: str = None,
        invoice_type: int = None,
        is_protocol: bool = None,
        is_share: bool = None,
        is_stop: bool = None,
        is_transfer: bool = None,
        meal_desc: str = None,
        oil_price: int = None,
        ota_item_id: str = None,
        price: int = None,
        product_type: int = None,
        product_type_desc: str = None,
        promotion_price: str = None,
        remained_seat_count: str = None,
        secret_params: str = None,
        segment_number: str = None,
        stop_arr_time: str = None,
        stop_city: str = None,
        stop_dep_time: str = None,
        ticket_price: int = None,
        total_price: str = None,
        trip_type: int = None,
    ):
        self.airline_info = airline_info
        self.arr_airport_info = arr_airport_info
        self.arr_date = arr_date
        self.build_price = build_price
        self.cabin = cabin
        self.cabin_class = cabin_class
        self.cabin_info_list = cabin_info_list
        self.carrier_airline = carrier_airline
        self.carrier_no = carrier_no
        self.dep_airport_info = dep_airport_info
        self.dep_city_code = dep_city_code
        self.dep_date = dep_date
        self.discount = discount
        self.flight_no = flight_no
        self.flight_rule_list = flight_rule_list
        self.flight_rule_list_str = flight_rule_list_str
        self.flight_size = flight_size
        self.flight_type = flight_type
        self.invoice_type = invoice_type
        self.is_protocol = is_protocol
        self.is_share = is_share
        self.is_stop = is_stop
        self.is_transfer = is_transfer
        self.meal_desc = meal_desc
        self.oil_price = oil_price
        self.ota_item_id = ota_item_id
        self.price = price
        self.product_type = product_type
        self.product_type_desc = product_type_desc
        self.promotion_price = promotion_price
        self.remained_seat_count = remained_seat_count
        self.secret_params = secret_params
        self.segment_number = segment_number
        self.stop_arr_time = stop_arr_time
        self.stop_city = stop_city
        self.stop_dep_time = stop_dep_time
        self.ticket_price = ticket_price
        self.total_price = total_price
        self.trip_type = trip_type

    def validate(self):
        if self.airline_info:
            self.airline_info.validate()
        if self.arr_airport_info:
            self.arr_airport_info.validate()
        if self.cabin_info_list:
            for v1 in self.cabin_info_list:
                 if v1:
                    v1.validate()
        if self.dep_airport_info:
            self.dep_airport_info.validate()
        if self.flight_rule_list:
            for v1 in self.flight_rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_info is not None:
            result['airline_info'] = self.airline_info.to_map()

        if self.arr_airport_info is not None:
            result['arr_airport_info'] = self.arr_airport_info.to_map()

        if self.arr_date is not None:
            result['arr_date'] = self.arr_date

        if self.build_price is not None:
            result['build_price'] = self.build_price

        if self.cabin is not None:
            result['cabin'] = self.cabin

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        result['cabin_info_list'] = []
        if self.cabin_info_list is not None:
            for k1 in self.cabin_info_list:
                result['cabin_info_list'].append(k1.to_map() if k1 else None)

        if self.carrier_airline is not None:
            result['carrier_airline'] = self.carrier_airline

        if self.carrier_no is not None:
            result['carrier_no'] = self.carrier_no

        if self.dep_airport_info is not None:
            result['dep_airport_info'] = self.dep_airport_info.to_map()

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_date is not None:
            result['dep_date'] = self.dep_date

        if self.discount is not None:
            result['discount'] = self.discount

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        result['flight_rule_list'] = []
        if self.flight_rule_list is not None:
            for k1 in self.flight_rule_list:
                result['flight_rule_list'].append(k1.to_map() if k1 else None)

        if self.flight_rule_list_str is not None:
            result['flight_rule_list_str'] = self.flight_rule_list_str

        if self.flight_size is not None:
            result['flight_size'] = self.flight_size

        if self.flight_type is not None:
            result['flight_type'] = self.flight_type

        if self.invoice_type is not None:
            result['invoice_type'] = self.invoice_type

        if self.is_protocol is not None:
            result['is_protocol'] = self.is_protocol

        if self.is_share is not None:
            result['is_share'] = self.is_share

        if self.is_stop is not None:
            result['is_stop'] = self.is_stop

        if self.is_transfer is not None:
            result['is_transfer'] = self.is_transfer

        if self.meal_desc is not None:
            result['meal_desc'] = self.meal_desc

        if self.oil_price is not None:
            result['oil_price'] = self.oil_price

        if self.ota_item_id is not None:
            result['ota_item_id'] = self.ota_item_id

        if self.price is not None:
            result['price'] = self.price

        if self.product_type is not None:
            result['product_type'] = self.product_type

        if self.product_type_desc is not None:
            result['product_type_desc'] = self.product_type_desc

        if self.promotion_price is not None:
            result['promotion_price'] = self.promotion_price

        if self.remained_seat_count is not None:
            result['remained_seat_count'] = self.remained_seat_count

        if self.secret_params is not None:
            result['secret_params'] = self.secret_params

        if self.segment_number is not None:
            result['segment_number'] = self.segment_number

        if self.stop_arr_time is not None:
            result['stop_arr_time'] = self.stop_arr_time

        if self.stop_city is not None:
            result['stop_city'] = self.stop_city

        if self.stop_dep_time is not None:
            result['stop_dep_time'] = self.stop_dep_time

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        if self.total_price is not None:
            result['total_price'] = self.total_price

        if self.trip_type is not None:
            result['trip_type'] = self.trip_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_info') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListAirlineInfo()
            self.airline_info = temp_model.from_map(m.get('airline_info'))

        if m.get('arr_airport_info') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListArrAirportInfo()
            self.arr_airport_info = temp_model.from_map(m.get('arr_airport_info'))

        if m.get('arr_date') is not None:
            self.arr_date = m.get('arr_date')

        if m.get('build_price') is not None:
            self.build_price = m.get('build_price')

        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        self.cabin_info_list = []
        if m.get('cabin_info_list') is not None:
            for k1 in m.get('cabin_info_list'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoList()
                self.cabin_info_list.append(temp_model.from_map(k1))

        if m.get('carrier_airline') is not None:
            self.carrier_airline = m.get('carrier_airline')

        if m.get('carrier_no') is not None:
            self.carrier_no = m.get('carrier_no')

        if m.get('dep_airport_info') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListDepAirportInfo()
            self.dep_airport_info = temp_model.from_map(m.get('dep_airport_info'))

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')

        if m.get('discount') is not None:
            self.discount = m.get('discount')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        self.flight_rule_list = []
        if m.get('flight_rule_list') is not None:
            for k1 in m.get('flight_rule_list'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleList()
                self.flight_rule_list.append(temp_model.from_map(k1))

        if m.get('flight_rule_list_str') is not None:
            self.flight_rule_list_str = m.get('flight_rule_list_str')

        if m.get('flight_size') is not None:
            self.flight_size = m.get('flight_size')

        if m.get('flight_type') is not None:
            self.flight_type = m.get('flight_type')

        if m.get('invoice_type') is not None:
            self.invoice_type = m.get('invoice_type')

        if m.get('is_protocol') is not None:
            self.is_protocol = m.get('is_protocol')

        if m.get('is_share') is not None:
            self.is_share = m.get('is_share')

        if m.get('is_stop') is not None:
            self.is_stop = m.get('is_stop')

        if m.get('is_transfer') is not None:
            self.is_transfer = m.get('is_transfer')

        if m.get('meal_desc') is not None:
            self.meal_desc = m.get('meal_desc')

        if m.get('oil_price') is not None:
            self.oil_price = m.get('oil_price')

        if m.get('ota_item_id') is not None:
            self.ota_item_id = m.get('ota_item_id')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('product_type') is not None:
            self.product_type = m.get('product_type')

        if m.get('product_type_desc') is not None:
            self.product_type_desc = m.get('product_type_desc')

        if m.get('promotion_price') is not None:
            self.promotion_price = m.get('promotion_price')

        if m.get('remained_seat_count') is not None:
            self.remained_seat_count = m.get('remained_seat_count')

        if m.get('secret_params') is not None:
            self.secret_params = m.get('secret_params')

        if m.get('segment_number') is not None:
            self.segment_number = m.get('segment_number')

        if m.get('stop_arr_time') is not None:
            self.stop_arr_time = m.get('stop_arr_time')

        if m.get('stop_city') is not None:
            self.stop_city = m.get('stop_city')

        if m.get('stop_dep_time') is not None:
            self.stop_dep_time = m.get('stop_dep_time')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        if m.get('total_price') is not None:
            self.total_price = m.get('total_price')

        if m.get('trip_type') is not None:
            self.trip_type = m.get('trip_type')

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleList(DaraModel):
    def __init__(
        self,
        baggage_info: str = None,
        baggage_item: main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListBaggageItem = None,
        change_rule: main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListChangeRule = None,
        change_rule_item: main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListChangeRuleItem = None,
        extra: str = None,
        refund_rule: main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListRefundRule = None,
        refund_rule_item: main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListRefundRuleItem = None,
        sign_rule: main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListSignRule = None,
        tuigaiqian_info: str = None,
        upgrade_rule: main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListUpgradeRule = None,
    ):
        self.baggage_info = baggage_info
        self.baggage_item = baggage_item
        self.change_rule = change_rule
        self.change_rule_item = change_rule_item
        self.extra = extra
        self.refund_rule = refund_rule
        self.refund_rule_item = refund_rule_item
        self.sign_rule = sign_rule
        self.tuigaiqian_info = tuigaiqian_info
        self.upgrade_rule = upgrade_rule

    def validate(self):
        if self.baggage_item:
            self.baggage_item.validate()
        if self.change_rule:
            self.change_rule.validate()
        if self.change_rule_item:
            self.change_rule_item.validate()
        if self.refund_rule:
            self.refund_rule.validate()
        if self.refund_rule_item:
            self.refund_rule_item.validate()
        if self.sign_rule:
            self.sign_rule.validate()
        if self.upgrade_rule:
            self.upgrade_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baggage_info is not None:
            result['baggage_info'] = self.baggage_info

        if self.baggage_item is not None:
            result['baggage_item'] = self.baggage_item.to_map()

        if self.change_rule is not None:
            result['change_rule'] = self.change_rule.to_map()

        if self.change_rule_item is not None:
            result['change_rule_item'] = self.change_rule_item.to_map()

        if self.extra is not None:
            result['extra'] = self.extra

        if self.refund_rule is not None:
            result['refund_rule'] = self.refund_rule.to_map()

        if self.refund_rule_item is not None:
            result['refund_rule_item'] = self.refund_rule_item.to_map()

        if self.sign_rule is not None:
            result['sign_rule'] = self.sign_rule.to_map()

        if self.tuigaiqian_info is not None:
            result['tuigaiqian_info'] = self.tuigaiqian_info

        if self.upgrade_rule is not None:
            result['upgrade_rule'] = self.upgrade_rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baggage_info') is not None:
            self.baggage_info = m.get('baggage_info')

        if m.get('baggage_item') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListBaggageItem()
            self.baggage_item = temp_model.from_map(m.get('baggage_item'))

        if m.get('change_rule') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListChangeRule()
            self.change_rule = temp_model.from_map(m.get('change_rule'))

        if m.get('change_rule_item') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListChangeRuleItem()
            self.change_rule_item = temp_model.from_map(m.get('change_rule_item'))

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('refund_rule') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListRefundRule()
            self.refund_rule = temp_model.from_map(m.get('refund_rule'))

        if m.get('refund_rule_item') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListRefundRuleItem()
            self.refund_rule_item = temp_model.from_map(m.get('refund_rule_item'))

        if m.get('sign_rule') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListSignRule()
            self.sign_rule = temp_model.from_map(m.get('sign_rule'))

        if m.get('tuigaiqian_info') is not None:
            self.tuigaiqian_info = m.get('tuigaiqian_info')

        if m.get('upgrade_rule') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListUpgradeRule()
            self.upgrade_rule = temp_model.from_map(m.get('upgrade_rule'))

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleListUpgradeRule(DaraModel):
    def __init__(
        self,
        able: bool = None,
        info: List[main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListUpgradeRuleInfo] = None,
    ):
        self.able = able
        self.info = info

    def validate(self):
        if self.info:
            for v1 in self.info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.able is not None:
            result['able'] = self.able

        result['info'] = []
        if self.info is not None:
            for k1 in self.info:
                result['info'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('able') is not None:
            self.able = m.get('able')

        self.info = []
        if m.get('info') is not None:
            for k1 in m.get('info'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListUpgradeRuleInfo()
                self.info.append(temp_model.from_map(k1))

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleListUpgradeRuleInfo(DaraModel):
    def __init__(
        self,
        content: str = None,
        cost: int = None,
        cost_percent: int = None,
        time_stamp: int = None,
        time_type: str = None,
        title: str = None,
    ):
        self.content = content
        self.cost = cost
        self.cost_percent = cost_percent
        self.time_stamp = time_stamp
        self.time_type = time_type
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.cost is not None:
            result['cost'] = self.cost

        if self.cost_percent is not None:
            result['cost_percent'] = self.cost_percent

        if self.time_stamp is not None:
            result['time_stamp'] = self.time_stamp

        if self.time_type is not None:
            result['time_type'] = self.time_type

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('cost') is not None:
            self.cost = m.get('cost')

        if m.get('cost_percent') is not None:
            self.cost_percent = m.get('cost_percent')

        if m.get('time_stamp') is not None:
            self.time_stamp = m.get('time_stamp')

        if m.get('time_type') is not None:
            self.time_type = m.get('time_type')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleListSignRule(DaraModel):
    def __init__(
        self,
        able: bool = None,
        info: List[main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListSignRuleInfo] = None,
    ):
        self.able = able
        self.info = info

    def validate(self):
        if self.info:
            for v1 in self.info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.able is not None:
            result['able'] = self.able

        result['info'] = []
        if self.info is not None:
            for k1 in self.info:
                result['info'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('able') is not None:
            self.able = m.get('able')

        self.info = []
        if m.get('info') is not None:
            for k1 in m.get('info'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListSignRuleInfo()
                self.info.append(temp_model.from_map(k1))

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleListSignRuleInfo(DaraModel):
    def __init__(
        self,
        content: str = None,
        cost: int = None,
        cost_percent: int = None,
        time_stamp: int = None,
        time_type: str = None,
        title: str = None,
    ):
        self.content = content
        self.cost = cost
        self.cost_percent = cost_percent
        self.time_stamp = time_stamp
        self.time_type = time_type
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.cost is not None:
            result['cost'] = self.cost

        if self.cost_percent is not None:
            result['cost_percent'] = self.cost_percent

        if self.time_stamp is not None:
            result['time_stamp'] = self.time_stamp

        if self.time_type is not None:
            result['time_type'] = self.time_type

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('cost') is not None:
            self.cost = m.get('cost')

        if m.get('cost_percent') is not None:
            self.cost_percent = m.get('cost_percent')

        if m.get('time_stamp') is not None:
            self.time_stamp = m.get('time_stamp')

        if m.get('time_type') is not None:
            self.time_type = m.get('time_type')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleListRefundRuleItem(DaraModel):
    def __init__(
        self,
        extra_contents: List[main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListRefundRuleItemExtraContents] = None,
        index: int = None,
        refund_sub_items: List[main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListRefundRuleItemRefundSubItems] = None,
        sub_table_head: List[str] = None,
        table_head: str = None,
        title: str = None,
        type: int = None,
    ):
        self.extra_contents = extra_contents
        self.index = index
        self.refund_sub_items = refund_sub_items
        self.sub_table_head = sub_table_head
        self.table_head = table_head
        self.title = title
        self.type = type

    def validate(self):
        if self.extra_contents:
            for v1 in self.extra_contents:
                 if v1:
                    v1.validate()
        if self.refund_sub_items:
            for v1 in self.refund_sub_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['extra_contents'] = []
        if self.extra_contents is not None:
            for k1 in self.extra_contents:
                result['extra_contents'].append(k1.to_map() if k1 else None)

        if self.index is not None:
            result['index'] = self.index

        result['refund_sub_items'] = []
        if self.refund_sub_items is not None:
            for k1 in self.refund_sub_items:
                result['refund_sub_items'].append(k1.to_map() if k1 else None)

        if self.sub_table_head is not None:
            result['sub_table_head'] = self.sub_table_head

        if self.table_head is not None:
            result['table_head'] = self.table_head

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.extra_contents = []
        if m.get('extra_contents') is not None:
            for k1 in m.get('extra_contents'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListRefundRuleItemExtraContents()
                self.extra_contents.append(temp_model.from_map(k1))

        if m.get('index') is not None:
            self.index = m.get('index')

        self.refund_sub_items = []
        if m.get('refund_sub_items') is not None:
            for k1 in m.get('refund_sub_items'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListRefundRuleItemRefundSubItems()
                self.refund_sub_items.append(temp_model.from_map(k1))

        if m.get('sub_table_head') is not None:
            self.sub_table_head = m.get('sub_table_head')

        if m.get('table_head') is not None:
            self.table_head = m.get('table_head')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleListRefundRuleItemRefundSubItems(DaraModel):
    def __init__(
        self,
        is_struct: bool = None,
        ptc: str = None,
        refund_sub_contents: List[main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListRefundRuleItemRefundSubItemsRefundSubContents] = None,
        title: str = None,
    ):
        self.is_struct = is_struct
        # PTC
        self.ptc = ptc
        self.refund_sub_contents = refund_sub_contents
        self.title = title

    def validate(self):
        if self.refund_sub_contents:
            for v1 in self.refund_sub_contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_struct is not None:
            result['is_struct'] = self.is_struct

        if self.ptc is not None:
            result['ptc'] = self.ptc

        result['refund_sub_contents'] = []
        if self.refund_sub_contents is not None:
            for k1 in self.refund_sub_contents:
                result['refund_sub_contents'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('is_struct') is not None:
            self.is_struct = m.get('is_struct')

        if m.get('ptc') is not None:
            self.ptc = m.get('ptc')

        self.refund_sub_contents = []
        if m.get('refund_sub_contents') is not None:
            for k1 in m.get('refund_sub_contents'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListRefundRuleItemRefundSubItemsRefundSubContents()
                self.refund_sub_contents.append(temp_model.from_map(k1))

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleListRefundRuleItemRefundSubItemsRefundSubContents(DaraModel):
    def __init__(
        self,
        fee_desc: str = None,
        fee_range: str = None,
        style: int = None,
    ):
        self.fee_desc = fee_desc
        self.fee_range = fee_range
        self.style = style

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fee_desc is not None:
            result['fee_desc'] = self.fee_desc

        if self.fee_range is not None:
            result['fee_range'] = self.fee_range

        if self.style is not None:
            result['style'] = self.style

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fee_desc') is not None:
            self.fee_desc = m.get('fee_desc')

        if m.get('fee_range') is not None:
            self.fee_range = m.get('fee_range')

        if m.get('style') is not None:
            self.style = m.get('style')

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleListRefundRuleItemExtraContents(DaraModel):
    def __init__(
        self,
        content: str = None,
        title: str = None,
    ):
        self.content = content
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleListRefundRule(DaraModel):
    def __init__(
        self,
        able: bool = None,
        info: List[main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListRefundRuleInfo] = None,
    ):
        self.able = able
        self.info = info

    def validate(self):
        if self.info:
            for v1 in self.info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.able is not None:
            result['able'] = self.able

        result['info'] = []
        if self.info is not None:
            for k1 in self.info:
                result['info'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('able') is not None:
            self.able = m.get('able')

        self.info = []
        if m.get('info') is not None:
            for k1 in m.get('info'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListRefundRuleInfo()
                self.info.append(temp_model.from_map(k1))

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleListRefundRuleInfo(DaraModel):
    def __init__(
        self,
        content: str = None,
        cost: int = None,
        cost_percent: int = None,
        time_stamp: int = None,
        time_type: str = None,
        title: str = None,
    ):
        self.content = content
        self.cost = cost
        self.cost_percent = cost_percent
        self.time_stamp = time_stamp
        self.time_type = time_type
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.cost is not None:
            result['cost'] = self.cost

        if self.cost_percent is not None:
            result['cost_percent'] = self.cost_percent

        if self.time_stamp is not None:
            result['time_stamp'] = self.time_stamp

        if self.time_type is not None:
            result['time_type'] = self.time_type

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('cost') is not None:
            self.cost = m.get('cost')

        if m.get('cost_percent') is not None:
            self.cost_percent = m.get('cost_percent')

        if m.get('time_stamp') is not None:
            self.time_stamp = m.get('time_stamp')

        if m.get('time_type') is not None:
            self.time_type = m.get('time_type')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleListChangeRuleItem(DaraModel):
    def __init__(
        self,
        extra_contents: List[main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListChangeRuleItemExtraContents] = None,
        index: int = None,
        refund_sub_items: List[main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListChangeRuleItemRefundSubItems] = None,
        sub_table_head: List[str] = None,
        table_head: str = None,
        title: str = None,
        type: int = None,
    ):
        self.extra_contents = extra_contents
        self.index = index
        self.refund_sub_items = refund_sub_items
        self.sub_table_head = sub_table_head
        self.table_head = table_head
        self.title = title
        self.type = type

    def validate(self):
        if self.extra_contents:
            for v1 in self.extra_contents:
                 if v1:
                    v1.validate()
        if self.refund_sub_items:
            for v1 in self.refund_sub_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['extra_contents'] = []
        if self.extra_contents is not None:
            for k1 in self.extra_contents:
                result['extra_contents'].append(k1.to_map() if k1 else None)

        if self.index is not None:
            result['index'] = self.index

        result['refund_sub_items'] = []
        if self.refund_sub_items is not None:
            for k1 in self.refund_sub_items:
                result['refund_sub_items'].append(k1.to_map() if k1 else None)

        if self.sub_table_head is not None:
            result['sub_table_head'] = self.sub_table_head

        if self.table_head is not None:
            result['table_head'] = self.table_head

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.extra_contents = []
        if m.get('extra_contents') is not None:
            for k1 in m.get('extra_contents'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListChangeRuleItemExtraContents()
                self.extra_contents.append(temp_model.from_map(k1))

        if m.get('index') is not None:
            self.index = m.get('index')

        self.refund_sub_items = []
        if m.get('refund_sub_items') is not None:
            for k1 in m.get('refund_sub_items'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListChangeRuleItemRefundSubItems()
                self.refund_sub_items.append(temp_model.from_map(k1))

        if m.get('sub_table_head') is not None:
            self.sub_table_head = m.get('sub_table_head')

        if m.get('table_head') is not None:
            self.table_head = m.get('table_head')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleListChangeRuleItemRefundSubItems(DaraModel):
    def __init__(
        self,
        is_struct: bool = None,
        ptc: str = None,
        refund_sub_contents: List[main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListChangeRuleItemRefundSubItemsRefundSubContents] = None,
        title: str = None,
    ):
        # isStruct : true
        self.is_struct = is_struct
        # PTC
        self.ptc = ptc
        self.refund_sub_contents = refund_sub_contents
        self.title = title

    def validate(self):
        if self.refund_sub_contents:
            for v1 in self.refund_sub_contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_struct is not None:
            result['is_struct'] = self.is_struct

        if self.ptc is not None:
            result['ptc'] = self.ptc

        result['refund_sub_contents'] = []
        if self.refund_sub_contents is not None:
            for k1 in self.refund_sub_contents:
                result['refund_sub_contents'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('is_struct') is not None:
            self.is_struct = m.get('is_struct')

        if m.get('ptc') is not None:
            self.ptc = m.get('ptc')

        self.refund_sub_contents = []
        if m.get('refund_sub_contents') is not None:
            for k1 in m.get('refund_sub_contents'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListChangeRuleItemRefundSubItemsRefundSubContents()
                self.refund_sub_contents.append(temp_model.from_map(k1))

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleListChangeRuleItemRefundSubItemsRefundSubContents(DaraModel):
    def __init__(
        self,
        fee_desc: str = None,
        fee_range: str = None,
        style: int = None,
    ):
        self.fee_desc = fee_desc
        self.fee_range = fee_range
        self.style = style

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fee_desc is not None:
            result['fee_desc'] = self.fee_desc

        if self.fee_range is not None:
            result['fee_range'] = self.fee_range

        if self.style is not None:
            result['style'] = self.style

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fee_desc') is not None:
            self.fee_desc = m.get('fee_desc')

        if m.get('fee_range') is not None:
            self.fee_range = m.get('fee_range')

        if m.get('style') is not None:
            self.style = m.get('style')

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleListChangeRuleItemExtraContents(DaraModel):
    def __init__(
        self,
        content: str = None,
        title: str = None,
    ):
        self.content = content
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleListChangeRule(DaraModel):
    def __init__(
        self,
        able: bool = None,
        info: List[main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListChangeRuleInfo] = None,
    ):
        self.able = able
        self.info = info

    def validate(self):
        if self.info:
            for v1 in self.info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.able is not None:
            result['able'] = self.able

        result['info'] = []
        if self.info is not None:
            for k1 in self.info:
                result['info'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('able') is not None:
            self.able = m.get('able')

        self.info = []
        if m.get('info') is not None:
            for k1 in m.get('info'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListChangeRuleInfo()
                self.info.append(temp_model.from_map(k1))

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleListChangeRuleInfo(DaraModel):
    def __init__(
        self,
        content: str = None,
        cost: int = None,
        cost_percent: int = None,
        time_stamp: int = None,
        time_type: str = None,
        title: str = None,
    ):
        self.content = content
        self.cost = cost
        self.cost_percent = cost_percent
        self.time_stamp = time_stamp
        self.time_type = time_type
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.cost is not None:
            result['cost'] = self.cost

        if self.cost_percent is not None:
            result['cost_percent'] = self.cost_percent

        if self.time_stamp is not None:
            result['time_stamp'] = self.time_stamp

        if self.time_type is not None:
            result['time_type'] = self.time_type

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('cost') is not None:
            self.cost = m.get('cost')

        if m.get('cost_percent') is not None:
            self.cost_percent = m.get('cost_percent')

        if m.get('time_stamp') is not None:
            self.time_stamp = m.get('time_stamp')

        if m.get('time_type') is not None:
            self.time_type = m.get('time_type')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleListBaggageItem(DaraModel):
    def __init__(
        self,
        baggage_sub_items: List[main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListBaggageItemBaggageSubItems] = None,
        index: int = None,
        table_head: str = None,
        tips: main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListBaggageItemTips = None,
        title: str = None,
        type: int = None,
    ):
        self.baggage_sub_items = baggage_sub_items
        self.index = index
        self.table_head = table_head
        self.tips = tips
        self.title = title
        self.type = type

    def validate(self):
        if self.baggage_sub_items:
            for v1 in self.baggage_sub_items:
                 if v1:
                    v1.validate()
        if self.tips:
            self.tips.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['baggage_sub_items'] = []
        if self.baggage_sub_items is not None:
            for k1 in self.baggage_sub_items:
                result['baggage_sub_items'].append(k1.to_map() if k1 else None)

        if self.index is not None:
            result['index'] = self.index

        if self.table_head is not None:
            result['table_head'] = self.table_head

        if self.tips is not None:
            result['tips'] = self.tips.to_map()

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.baggage_sub_items = []
        if m.get('baggage_sub_items') is not None:
            for k1 in m.get('baggage_sub_items'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListBaggageItemBaggageSubItems()
                self.baggage_sub_items.append(temp_model.from_map(k1))

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('table_head') is not None:
            self.table_head = m.get('table_head')

        if m.get('tips') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListBaggageItemTips()
            self.tips = temp_model.from_map(m.get('tips'))

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleListBaggageItemTips(DaraModel):
    def __init__(
        self,
        logo: str = None,
        tips_desc: str = None,
        tips_image: str = None,
    ):
        self.logo = logo
        self.tips_desc = tips_desc
        self.tips_image = tips_image

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logo is not None:
            result['logo'] = self.logo

        if self.tips_desc is not None:
            result['tips_desc'] = self.tips_desc

        if self.tips_image is not None:
            result['tips_image'] = self.tips_image

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logo') is not None:
            self.logo = m.get('logo')

        if m.get('tips_desc') is not None:
            self.tips_desc = m.get('tips_desc')

        if m.get('tips_image') is not None:
            self.tips_image = m.get('tips_image')

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleListBaggageItemBaggageSubItems(DaraModel):
    def __init__(
        self,
        baggage_sub_content_visualizes: List[main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListBaggageItemBaggageSubItemsBaggageSubContentVisualizes] = None,
        extra_content_visualizes: List[Any] = None,
        is_struct: bool = None,
        ptc: str = None,
        title: str = None,
    ):
        self.baggage_sub_content_visualizes = baggage_sub_content_visualizes
        self.extra_content_visualizes = extra_content_visualizes
        self.is_struct = is_struct
        # PTC
        self.ptc = ptc
        self.title = title

    def validate(self):
        if self.baggage_sub_content_visualizes:
            for v1 in self.baggage_sub_content_visualizes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['baggage_sub_content_visualizes'] = []
        if self.baggage_sub_content_visualizes is not None:
            for k1 in self.baggage_sub_content_visualizes:
                result['baggage_sub_content_visualizes'].append(k1.to_map() if k1 else None)

        if self.extra_content_visualizes is not None:
            result['extra_content_visualizes'] = self.extra_content_visualizes

        if self.is_struct is not None:
            result['is_struct'] = self.is_struct

        if self.ptc is not None:
            result['ptc'] = self.ptc

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.baggage_sub_content_visualizes = []
        if m.get('baggage_sub_content_visualizes') is not None:
            for k1 in m.get('baggage_sub_content_visualizes'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListBaggageItemBaggageSubItemsBaggageSubContentVisualizes()
                self.baggage_sub_content_visualizes.append(temp_model.from_map(k1))

        if m.get('extra_content_visualizes') is not None:
            self.extra_content_visualizes = m.get('extra_content_visualizes')

        if m.get('is_struct') is not None:
            self.is_struct = m.get('is_struct')

        if m.get('ptc') is not None:
            self.ptc = m.get('ptc')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleListBaggageItemBaggageSubItemsBaggageSubContentVisualizes(DaraModel):
    def __init__(
        self,
        baggage_desc: List[str] = None,
        baggage_sub_content_type: int = None,
        description: main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListBaggageItemBaggageSubItemsBaggageSubContentVisualizesDescription = None,
        image_do: main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListBaggageItemBaggageSubItemsBaggageSubContentVisualizesImageDO = None,
        is_highlight: bool = None,
        sub_title: str = None,
    ):
        self.baggage_desc = baggage_desc
        self.baggage_sub_content_type = baggage_sub_content_type
        self.description = description
        self.image_do = image_do
        self.is_highlight = is_highlight
        self.sub_title = sub_title

    def validate(self):
        if self.description:
            self.description.validate()
        if self.image_do:
            self.image_do.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baggage_desc is not None:
            result['baggage_desc'] = self.baggage_desc

        if self.baggage_sub_content_type is not None:
            result['baggage_sub_content_type'] = self.baggage_sub_content_type

        if self.description is not None:
            result['description'] = self.description.to_map()

        if self.image_do is not None:
            result['image_d_o'] = self.image_do.to_map()

        if self.is_highlight is not None:
            result['is_highlight'] = self.is_highlight

        if self.sub_title is not None:
            result['sub_title'] = self.sub_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baggage_desc') is not None:
            self.baggage_desc = m.get('baggage_desc')

        if m.get('baggage_sub_content_type') is not None:
            self.baggage_sub_content_type = m.get('baggage_sub_content_type')

        if m.get('description') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListBaggageItemBaggageSubItemsBaggageSubContentVisualizesDescription()
            self.description = temp_model.from_map(m.get('description'))

        if m.get('image_d_o') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListFlightRuleListBaggageItemBaggageSubItemsBaggageSubContentVisualizesImageDO()
            self.image_do = temp_model.from_map(m.get('image_d_o'))

        if m.get('is_highlight') is not None:
            self.is_highlight = m.get('is_highlight')

        if m.get('sub_title') is not None:
            self.sub_title = m.get('sub_title')

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleListBaggageItemBaggageSubItemsBaggageSubContentVisualizesImageDO(DaraModel):
    def __init__(
        self,
        image: str = None,
        largest: str = None,
        middle: str = None,
        smallest: str = None,
    ):
        self.image = image
        self.largest = largest
        self.middle = middle
        self.smallest = smallest

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image is not None:
            result['image'] = self.image

        if self.largest is not None:
            result['largest'] = self.largest

        if self.middle is not None:
            result['middle'] = self.middle

        if self.smallest is not None:
            result['smallest'] = self.smallest

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('largest') is not None:
            self.largest = m.get('largest')

        if m.get('middle') is not None:
            self.middle = m.get('middle')

        if m.get('smallest') is not None:
            self.smallest = m.get('smallest')

        return self

class FlightOtaSearchResponseBodyModuleFlightListFlightRuleListBaggageItemBaggageSubItemsBaggageSubContentVisualizesDescription(DaraModel):
    def __init__(
        self,
        desc: str = None,
        icon: str = None,
        image: str = None,
        title: str = None,
    ):
        self.desc = desc
        self.icon = icon
        self.image = image
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['desc'] = self.desc

        if self.icon is not None:
            result['icon'] = self.icon

        if self.image is not None:
            result['image'] = self.image

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('icon') is not None:
            self.icon = m.get('icon')

        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaSearchResponseBodyModuleFlightListDepAirportInfo(DaraModel):
    def __init__(
        self,
        airport_code: str = None,
        airport_name: str = None,
        city_code: str = None,
        city_name: str = None,
        terminal: str = None,
    ):
        self.airport_code = airport_code
        self.airport_name = airport_name
        self.city_code = city_code
        self.city_name = city_name
        self.terminal = terminal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airport_code is not None:
            result['airport_code'] = self.airport_code

        if self.airport_name is not None:
            result['airport_name'] = self.airport_name

        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.city_name is not None:
            result['city_name'] = self.city_name

        if self.terminal is not None:
            result['terminal'] = self.terminal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airport_code') is not None:
            self.airport_code = m.get('airport_code')

        if m.get('airport_name') is not None:
            self.airport_name = m.get('airport_name')

        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')

        if m.get('terminal') is not None:
            self.terminal = m.get('terminal')

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoList(DaraModel):
    def __init__(
        self,
        agent_id: int = None,
        basic_cabin_price: int = None,
        build_price: int = None,
        cabin: str = None,
        cabin_class: str = None,
        cabin_class_name: str = None,
        child_cabin: str = None,
        class_name: str = None,
        class_rule: str = None,
        discount: str = None,
        flight_rule_list: List[main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleList] = None,
        flight_rule_list_str: str = None,
        invoice_type: int = None,
        is_protocol: bool = None,
        oil_price: int = None,
        order_params: str = None,
        ota_item_id: str = None,
        price: int = None,
        product_type: int = None,
        product_type_desc: str = None,
        promotion_price: str = None,
        remained_seat_count: str = None,
        ticket_price: int = None,
        total_price: int = None,
    ):
        self.agent_id = agent_id
        self.basic_cabin_price = basic_cabin_price
        self.build_price = build_price
        self.cabin = cabin
        self.cabin_class = cabin_class
        self.cabin_class_name = cabin_class_name
        self.child_cabin = child_cabin
        self.class_name = class_name
        self.class_rule = class_rule
        self.discount = discount
        self.flight_rule_list = flight_rule_list
        self.flight_rule_list_str = flight_rule_list_str
        self.invoice_type = invoice_type
        self.is_protocol = is_protocol
        self.oil_price = oil_price
        self.order_params = order_params
        self.ota_item_id = ota_item_id
        self.price = price
        self.product_type = product_type
        self.product_type_desc = product_type_desc
        self.promotion_price = promotion_price
        self.remained_seat_count = remained_seat_count
        self.ticket_price = ticket_price
        self.total_price = total_price

    def validate(self):
        if self.flight_rule_list:
            for v1 in self.flight_rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agent_id'] = self.agent_id

        if self.basic_cabin_price is not None:
            result['basic_cabin_price'] = self.basic_cabin_price

        if self.build_price is not None:
            result['build_price'] = self.build_price

        if self.cabin is not None:
            result['cabin'] = self.cabin

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.cabin_class_name is not None:
            result['cabin_class_name'] = self.cabin_class_name

        if self.child_cabin is not None:
            result['child_cabin'] = self.child_cabin

        if self.class_name is not None:
            result['class_name'] = self.class_name

        if self.class_rule is not None:
            result['class_rule'] = self.class_rule

        if self.discount is not None:
            result['discount'] = self.discount

        result['flight_rule_list'] = []
        if self.flight_rule_list is not None:
            for k1 in self.flight_rule_list:
                result['flight_rule_list'].append(k1.to_map() if k1 else None)

        if self.flight_rule_list_str is not None:
            result['flight_rule_list_str'] = self.flight_rule_list_str

        if self.invoice_type is not None:
            result['invoice_type'] = self.invoice_type

        if self.is_protocol is not None:
            result['is_protocol'] = self.is_protocol

        if self.oil_price is not None:
            result['oil_price'] = self.oil_price

        if self.order_params is not None:
            result['order_params'] = self.order_params

        if self.ota_item_id is not None:
            result['ota_item_id'] = self.ota_item_id

        if self.price is not None:
            result['price'] = self.price

        if self.product_type is not None:
            result['product_type'] = self.product_type

        if self.product_type_desc is not None:
            result['product_type_desc'] = self.product_type_desc

        if self.promotion_price is not None:
            result['promotion_price'] = self.promotion_price

        if self.remained_seat_count is not None:
            result['remained_seat_count'] = self.remained_seat_count

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        if self.total_price is not None:
            result['total_price'] = self.total_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_id') is not None:
            self.agent_id = m.get('agent_id')

        if m.get('basic_cabin_price') is not None:
            self.basic_cabin_price = m.get('basic_cabin_price')

        if m.get('build_price') is not None:
            self.build_price = m.get('build_price')

        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('cabin_class_name') is not None:
            self.cabin_class_name = m.get('cabin_class_name')

        if m.get('child_cabin') is not None:
            self.child_cabin = m.get('child_cabin')

        if m.get('class_name') is not None:
            self.class_name = m.get('class_name')

        if m.get('class_rule') is not None:
            self.class_rule = m.get('class_rule')

        if m.get('discount') is not None:
            self.discount = m.get('discount')

        self.flight_rule_list = []
        if m.get('flight_rule_list') is not None:
            for k1 in m.get('flight_rule_list'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleList()
                self.flight_rule_list.append(temp_model.from_map(k1))

        if m.get('flight_rule_list_str') is not None:
            self.flight_rule_list_str = m.get('flight_rule_list_str')

        if m.get('invoice_type') is not None:
            self.invoice_type = m.get('invoice_type')

        if m.get('is_protocol') is not None:
            self.is_protocol = m.get('is_protocol')

        if m.get('oil_price') is not None:
            self.oil_price = m.get('oil_price')

        if m.get('order_params') is not None:
            self.order_params = m.get('order_params')

        if m.get('ota_item_id') is not None:
            self.ota_item_id = m.get('ota_item_id')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('product_type') is not None:
            self.product_type = m.get('product_type')

        if m.get('product_type_desc') is not None:
            self.product_type_desc = m.get('product_type_desc')

        if m.get('promotion_price') is not None:
            self.promotion_price = m.get('promotion_price')

        if m.get('remained_seat_count') is not None:
            self.remained_seat_count = m.get('remained_seat_count')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        if m.get('total_price') is not None:
            self.total_price = m.get('total_price')

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleList(DaraModel):
    def __init__(
        self,
        baggage_info: str = None,
        baggage_item: main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListBaggageItem = None,
        change_rule: main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListChangeRule = None,
        change_rule_item: main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListChangeRuleItem = None,
        extra: str = None,
        refund_rule: main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListRefundRule = None,
        refund_rule_item: main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListRefundRuleItem = None,
        sign_rule: main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListSignRule = None,
        tuigaiqian_info: str = None,
        upgrade_rule: main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListUpgradeRule = None,
    ):
        self.baggage_info = baggage_info
        self.baggage_item = baggage_item
        self.change_rule = change_rule
        self.change_rule_item = change_rule_item
        self.extra = extra
        self.refund_rule = refund_rule
        self.refund_rule_item = refund_rule_item
        self.sign_rule = sign_rule
        self.tuigaiqian_info = tuigaiqian_info
        self.upgrade_rule = upgrade_rule

    def validate(self):
        if self.baggage_item:
            self.baggage_item.validate()
        if self.change_rule:
            self.change_rule.validate()
        if self.change_rule_item:
            self.change_rule_item.validate()
        if self.refund_rule:
            self.refund_rule.validate()
        if self.refund_rule_item:
            self.refund_rule_item.validate()
        if self.sign_rule:
            self.sign_rule.validate()
        if self.upgrade_rule:
            self.upgrade_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baggage_info is not None:
            result['baggage_info'] = self.baggage_info

        if self.baggage_item is not None:
            result['baggage_item'] = self.baggage_item.to_map()

        if self.change_rule is not None:
            result['change_rule'] = self.change_rule.to_map()

        if self.change_rule_item is not None:
            result['change_rule_item'] = self.change_rule_item.to_map()

        if self.extra is not None:
            result['extra'] = self.extra

        if self.refund_rule is not None:
            result['refund_rule'] = self.refund_rule.to_map()

        if self.refund_rule_item is not None:
            result['refund_rule_item'] = self.refund_rule_item.to_map()

        if self.sign_rule is not None:
            result['sign_rule'] = self.sign_rule.to_map()

        if self.tuigaiqian_info is not None:
            result['tuigaiqian_info'] = self.tuigaiqian_info

        if self.upgrade_rule is not None:
            result['upgrade_rule'] = self.upgrade_rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baggage_info') is not None:
            self.baggage_info = m.get('baggage_info')

        if m.get('baggage_item') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListBaggageItem()
            self.baggage_item = temp_model.from_map(m.get('baggage_item'))

        if m.get('change_rule') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListChangeRule()
            self.change_rule = temp_model.from_map(m.get('change_rule'))

        if m.get('change_rule_item') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListChangeRuleItem()
            self.change_rule_item = temp_model.from_map(m.get('change_rule_item'))

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('refund_rule') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListRefundRule()
            self.refund_rule = temp_model.from_map(m.get('refund_rule'))

        if m.get('refund_rule_item') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListRefundRuleItem()
            self.refund_rule_item = temp_model.from_map(m.get('refund_rule_item'))

        if m.get('sign_rule') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListSignRule()
            self.sign_rule = temp_model.from_map(m.get('sign_rule'))

        if m.get('tuigaiqian_info') is not None:
            self.tuigaiqian_info = m.get('tuigaiqian_info')

        if m.get('upgrade_rule') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListUpgradeRule()
            self.upgrade_rule = temp_model.from_map(m.get('upgrade_rule'))

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListUpgradeRule(DaraModel):
    def __init__(
        self,
        able: bool = None,
        info: List[main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListUpgradeRuleInfo] = None,
    ):
        self.able = able
        self.info = info

    def validate(self):
        if self.info:
            for v1 in self.info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.able is not None:
            result['able'] = self.able

        result['info'] = []
        if self.info is not None:
            for k1 in self.info:
                result['info'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('able') is not None:
            self.able = m.get('able')

        self.info = []
        if m.get('info') is not None:
            for k1 in m.get('info'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListUpgradeRuleInfo()
                self.info.append(temp_model.from_map(k1))

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListUpgradeRuleInfo(DaraModel):
    def __init__(
        self,
        content: str = None,
        cost: int = None,
        cost_percent: int = None,
        time_stamp: int = None,
        time_type: str = None,
        title: str = None,
    ):
        self.content = content
        self.cost = cost
        self.cost_percent = cost_percent
        self.time_stamp = time_stamp
        self.time_type = time_type
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.cost is not None:
            result['cost'] = self.cost

        if self.cost_percent is not None:
            result['cost_percent'] = self.cost_percent

        if self.time_stamp is not None:
            result['time_stamp'] = self.time_stamp

        if self.time_type is not None:
            result['time_type'] = self.time_type

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('cost') is not None:
            self.cost = m.get('cost')

        if m.get('cost_percent') is not None:
            self.cost_percent = m.get('cost_percent')

        if m.get('time_stamp') is not None:
            self.time_stamp = m.get('time_stamp')

        if m.get('time_type') is not None:
            self.time_type = m.get('time_type')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListSignRule(DaraModel):
    def __init__(
        self,
        able: bool = None,
        info: List[main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListSignRuleInfo] = None,
    ):
        self.able = able
        self.info = info

    def validate(self):
        if self.info:
            for v1 in self.info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.able is not None:
            result['able'] = self.able

        result['info'] = []
        if self.info is not None:
            for k1 in self.info:
                result['info'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('able') is not None:
            self.able = m.get('able')

        self.info = []
        if m.get('info') is not None:
            for k1 in m.get('info'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListSignRuleInfo()
                self.info.append(temp_model.from_map(k1))

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListSignRuleInfo(DaraModel):
    def __init__(
        self,
        content: str = None,
        cost: int = None,
        cost_percent: int = None,
        time_stamp: int = None,
        time_type: str = None,
        title: str = None,
    ):
        self.content = content
        self.cost = cost
        self.cost_percent = cost_percent
        self.time_stamp = time_stamp
        self.time_type = time_type
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.cost is not None:
            result['cost'] = self.cost

        if self.cost_percent is not None:
            result['cost_percent'] = self.cost_percent

        if self.time_stamp is not None:
            result['time_stamp'] = self.time_stamp

        if self.time_type is not None:
            result['time_type'] = self.time_type

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('cost') is not None:
            self.cost = m.get('cost')

        if m.get('cost_percent') is not None:
            self.cost_percent = m.get('cost_percent')

        if m.get('time_stamp') is not None:
            self.time_stamp = m.get('time_stamp')

        if m.get('time_type') is not None:
            self.time_type = m.get('time_type')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListRefundRuleItem(DaraModel):
    def __init__(
        self,
        extra_contents: List[main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListRefundRuleItemExtraContents] = None,
        index: int = None,
        refund_sub_items: List[main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListRefundRuleItemRefundSubItems] = None,
        sub_table_head: List[str] = None,
        table_head: str = None,
        title: str = None,
        type: int = None,
    ):
        self.extra_contents = extra_contents
        self.index = index
        self.refund_sub_items = refund_sub_items
        self.sub_table_head = sub_table_head
        self.table_head = table_head
        self.title = title
        self.type = type

    def validate(self):
        if self.extra_contents:
            for v1 in self.extra_contents:
                 if v1:
                    v1.validate()
        if self.refund_sub_items:
            for v1 in self.refund_sub_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['extra_contents'] = []
        if self.extra_contents is not None:
            for k1 in self.extra_contents:
                result['extra_contents'].append(k1.to_map() if k1 else None)

        if self.index is not None:
            result['index'] = self.index

        result['refund_sub_items'] = []
        if self.refund_sub_items is not None:
            for k1 in self.refund_sub_items:
                result['refund_sub_items'].append(k1.to_map() if k1 else None)

        if self.sub_table_head is not None:
            result['sub_table_head'] = self.sub_table_head

        if self.table_head is not None:
            result['table_head'] = self.table_head

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.extra_contents = []
        if m.get('extra_contents') is not None:
            for k1 in m.get('extra_contents'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListRefundRuleItemExtraContents()
                self.extra_contents.append(temp_model.from_map(k1))

        if m.get('index') is not None:
            self.index = m.get('index')

        self.refund_sub_items = []
        if m.get('refund_sub_items') is not None:
            for k1 in m.get('refund_sub_items'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListRefundRuleItemRefundSubItems()
                self.refund_sub_items.append(temp_model.from_map(k1))

        if m.get('sub_table_head') is not None:
            self.sub_table_head = m.get('sub_table_head')

        if m.get('table_head') is not None:
            self.table_head = m.get('table_head')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListRefundRuleItemRefundSubItems(DaraModel):
    def __init__(
        self,
        is_struct: bool = None,
        ptc: str = None,
        refund_sub_contents: List[main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListRefundRuleItemRefundSubItemsRefundSubContents] = None,
        title: str = None,
    ):
        self.is_struct = is_struct
        # PTC
        self.ptc = ptc
        self.refund_sub_contents = refund_sub_contents
        self.title = title

    def validate(self):
        if self.refund_sub_contents:
            for v1 in self.refund_sub_contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_struct is not None:
            result['is_struct'] = self.is_struct

        if self.ptc is not None:
            result['ptc'] = self.ptc

        result['refund_sub_contents'] = []
        if self.refund_sub_contents is not None:
            for k1 in self.refund_sub_contents:
                result['refund_sub_contents'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('is_struct') is not None:
            self.is_struct = m.get('is_struct')

        if m.get('ptc') is not None:
            self.ptc = m.get('ptc')

        self.refund_sub_contents = []
        if m.get('refund_sub_contents') is not None:
            for k1 in m.get('refund_sub_contents'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListRefundRuleItemRefundSubItemsRefundSubContents()
                self.refund_sub_contents.append(temp_model.from_map(k1))

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListRefundRuleItemRefundSubItemsRefundSubContents(DaraModel):
    def __init__(
        self,
        fee_desc: str = None,
        fee_range: str = None,
        style: int = None,
    ):
        self.fee_desc = fee_desc
        self.fee_range = fee_range
        self.style = style

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fee_desc is not None:
            result['fee_desc'] = self.fee_desc

        if self.fee_range is not None:
            result['fee_range'] = self.fee_range

        if self.style is not None:
            result['style'] = self.style

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fee_desc') is not None:
            self.fee_desc = m.get('fee_desc')

        if m.get('fee_range') is not None:
            self.fee_range = m.get('fee_range')

        if m.get('style') is not None:
            self.style = m.get('style')

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListRefundRuleItemExtraContents(DaraModel):
    def __init__(
        self,
        content: str = None,
        title: str = None,
    ):
        self.content = content
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListRefundRule(DaraModel):
    def __init__(
        self,
        able: bool = None,
        info: List[main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListRefundRuleInfo] = None,
    ):
        self.able = able
        self.info = info

    def validate(self):
        if self.info:
            for v1 in self.info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.able is not None:
            result['able'] = self.able

        result['info'] = []
        if self.info is not None:
            for k1 in self.info:
                result['info'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('able') is not None:
            self.able = m.get('able')

        self.info = []
        if m.get('info') is not None:
            for k1 in m.get('info'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListRefundRuleInfo()
                self.info.append(temp_model.from_map(k1))

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListRefundRuleInfo(DaraModel):
    def __init__(
        self,
        content: str = None,
        cost: int = None,
        cost_percent: int = None,
        time_stamp: int = None,
        time_type: str = None,
        title: str = None,
    ):
        self.content = content
        self.cost = cost
        self.cost_percent = cost_percent
        self.time_stamp = time_stamp
        self.time_type = time_type
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.cost is not None:
            result['cost'] = self.cost

        if self.cost_percent is not None:
            result['cost_percent'] = self.cost_percent

        if self.time_stamp is not None:
            result['time_stamp'] = self.time_stamp

        if self.time_type is not None:
            result['time_type'] = self.time_type

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('cost') is not None:
            self.cost = m.get('cost')

        if m.get('cost_percent') is not None:
            self.cost_percent = m.get('cost_percent')

        if m.get('time_stamp') is not None:
            self.time_stamp = m.get('time_stamp')

        if m.get('time_type') is not None:
            self.time_type = m.get('time_type')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListChangeRuleItem(DaraModel):
    def __init__(
        self,
        extra_contents: List[main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListChangeRuleItemExtraContents] = None,
        index: int = None,
        refund_sub_items: List[main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListChangeRuleItemRefundSubItems] = None,
        sub_table_head: List[str] = None,
        table_head: str = None,
        title: str = None,
        type: int = None,
    ):
        self.extra_contents = extra_contents
        self.index = index
        self.refund_sub_items = refund_sub_items
        self.sub_table_head = sub_table_head
        self.table_head = table_head
        self.title = title
        self.type = type

    def validate(self):
        if self.extra_contents:
            for v1 in self.extra_contents:
                 if v1:
                    v1.validate()
        if self.refund_sub_items:
            for v1 in self.refund_sub_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['extra_contents'] = []
        if self.extra_contents is not None:
            for k1 in self.extra_contents:
                result['extra_contents'].append(k1.to_map() if k1 else None)

        if self.index is not None:
            result['index'] = self.index

        result['refund_sub_items'] = []
        if self.refund_sub_items is not None:
            for k1 in self.refund_sub_items:
                result['refund_sub_items'].append(k1.to_map() if k1 else None)

        if self.sub_table_head is not None:
            result['sub_table_head'] = self.sub_table_head

        if self.table_head is not None:
            result['table_head'] = self.table_head

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.extra_contents = []
        if m.get('extra_contents') is not None:
            for k1 in m.get('extra_contents'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListChangeRuleItemExtraContents()
                self.extra_contents.append(temp_model.from_map(k1))

        if m.get('index') is not None:
            self.index = m.get('index')

        self.refund_sub_items = []
        if m.get('refund_sub_items') is not None:
            for k1 in m.get('refund_sub_items'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListChangeRuleItemRefundSubItems()
                self.refund_sub_items.append(temp_model.from_map(k1))

        if m.get('sub_table_head') is not None:
            self.sub_table_head = m.get('sub_table_head')

        if m.get('table_head') is not None:
            self.table_head = m.get('table_head')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListChangeRuleItemRefundSubItems(DaraModel):
    def __init__(
        self,
        is_struct: bool = None,
        ptc: str = None,
        refund_sub_contents: List[main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListChangeRuleItemRefundSubItemsRefundSubContents] = None,
        title: str = None,
    ):
        self.is_struct = is_struct
        # PTC
        self.ptc = ptc
        self.refund_sub_contents = refund_sub_contents
        self.title = title

    def validate(self):
        if self.refund_sub_contents:
            for v1 in self.refund_sub_contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_struct is not None:
            result['is_struct'] = self.is_struct

        if self.ptc is not None:
            result['ptc'] = self.ptc

        result['refund_sub_contents'] = []
        if self.refund_sub_contents is not None:
            for k1 in self.refund_sub_contents:
                result['refund_sub_contents'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('is_struct') is not None:
            self.is_struct = m.get('is_struct')

        if m.get('ptc') is not None:
            self.ptc = m.get('ptc')

        self.refund_sub_contents = []
        if m.get('refund_sub_contents') is not None:
            for k1 in m.get('refund_sub_contents'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListChangeRuleItemRefundSubItemsRefundSubContents()
                self.refund_sub_contents.append(temp_model.from_map(k1))

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListChangeRuleItemRefundSubItemsRefundSubContents(DaraModel):
    def __init__(
        self,
        fee_desc: str = None,
        fee_range: str = None,
        style: int = None,
    ):
        self.fee_desc = fee_desc
        self.fee_range = fee_range
        self.style = style

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fee_desc is not None:
            result['fee_desc'] = self.fee_desc

        if self.fee_range is not None:
            result['fee_range'] = self.fee_range

        if self.style is not None:
            result['style'] = self.style

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fee_desc') is not None:
            self.fee_desc = m.get('fee_desc')

        if m.get('fee_range') is not None:
            self.fee_range = m.get('fee_range')

        if m.get('style') is not None:
            self.style = m.get('style')

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListChangeRuleItemExtraContents(DaraModel):
    def __init__(
        self,
        content: str = None,
        title: str = None,
    ):
        self.content = content
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListChangeRule(DaraModel):
    def __init__(
        self,
        able: bool = None,
        info: List[main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListChangeRuleInfo] = None,
    ):
        self.able = able
        self.info = info

    def validate(self):
        if self.info:
            for v1 in self.info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.able is not None:
            result['able'] = self.able

        result['info'] = []
        if self.info is not None:
            for k1 in self.info:
                result['info'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('able') is not None:
            self.able = m.get('able')

        self.info = []
        if m.get('info') is not None:
            for k1 in m.get('info'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListChangeRuleInfo()
                self.info.append(temp_model.from_map(k1))

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListChangeRuleInfo(DaraModel):
    def __init__(
        self,
        content: str = None,
        cost: int = None,
        cost_percent: int = None,
        time_stamp: int = None,
        time_type: str = None,
        title: str = None,
    ):
        self.content = content
        self.cost = cost
        self.cost_percent = cost_percent
        self.time_stamp = time_stamp
        self.time_type = time_type
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.cost is not None:
            result['cost'] = self.cost

        if self.cost_percent is not None:
            result['cost_percent'] = self.cost_percent

        if self.time_stamp is not None:
            result['time_stamp'] = self.time_stamp

        if self.time_type is not None:
            result['time_type'] = self.time_type

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('cost') is not None:
            self.cost = m.get('cost')

        if m.get('cost_percent') is not None:
            self.cost_percent = m.get('cost_percent')

        if m.get('time_stamp') is not None:
            self.time_stamp = m.get('time_stamp')

        if m.get('time_type') is not None:
            self.time_type = m.get('time_type')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListBaggageItem(DaraModel):
    def __init__(
        self,
        baggage_sub_items: List[main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListBaggageItemBaggageSubItems] = None,
        index: int = None,
        table_head: str = None,
        tips: main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListBaggageItemTips = None,
        title: str = None,
        type: int = None,
    ):
        self.baggage_sub_items = baggage_sub_items
        self.index = index
        self.table_head = table_head
        self.tips = tips
        self.title = title
        self.type = type

    def validate(self):
        if self.baggage_sub_items:
            for v1 in self.baggage_sub_items:
                 if v1:
                    v1.validate()
        if self.tips:
            self.tips.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['baggage_sub_items'] = []
        if self.baggage_sub_items is not None:
            for k1 in self.baggage_sub_items:
                result['baggage_sub_items'].append(k1.to_map() if k1 else None)

        if self.index is not None:
            result['index'] = self.index

        if self.table_head is not None:
            result['table_head'] = self.table_head

        if self.tips is not None:
            result['tips'] = self.tips.to_map()

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.baggage_sub_items = []
        if m.get('baggage_sub_items') is not None:
            for k1 in m.get('baggage_sub_items'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListBaggageItemBaggageSubItems()
                self.baggage_sub_items.append(temp_model.from_map(k1))

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('table_head') is not None:
            self.table_head = m.get('table_head')

        if m.get('tips') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListBaggageItemTips()
            self.tips = temp_model.from_map(m.get('tips'))

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListBaggageItemTips(DaraModel):
    def __init__(
        self,
        logo: str = None,
        tips_desc: str = None,
        tips_image: str = None,
    ):
        self.logo = logo
        self.tips_desc = tips_desc
        self.tips_image = tips_image

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logo is not None:
            result['logo'] = self.logo

        if self.tips_desc is not None:
            result['tips_desc'] = self.tips_desc

        if self.tips_image is not None:
            result['tips_image'] = self.tips_image

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logo') is not None:
            self.logo = m.get('logo')

        if m.get('tips_desc') is not None:
            self.tips_desc = m.get('tips_desc')

        if m.get('tips_image') is not None:
            self.tips_image = m.get('tips_image')

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListBaggageItemBaggageSubItems(DaraModel):
    def __init__(
        self,
        baggage_sub_content_visualizes: List[main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListBaggageItemBaggageSubItemsBaggageSubContentVisualizes] = None,
        extra_content_visualizes: List[Any] = None,
        is_struct: bool = None,
        ptc: str = None,
        title: str = None,
    ):
        self.baggage_sub_content_visualizes = baggage_sub_content_visualizes
        self.extra_content_visualizes = extra_content_visualizes
        self.is_struct = is_struct
        # PTC
        self.ptc = ptc
        self.title = title

    def validate(self):
        if self.baggage_sub_content_visualizes:
            for v1 in self.baggage_sub_content_visualizes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['baggage_sub_content_visualizes'] = []
        if self.baggage_sub_content_visualizes is not None:
            for k1 in self.baggage_sub_content_visualizes:
                result['baggage_sub_content_visualizes'].append(k1.to_map() if k1 else None)

        if self.extra_content_visualizes is not None:
            result['extra_content_visualizes'] = self.extra_content_visualizes

        if self.is_struct is not None:
            result['is_struct'] = self.is_struct

        if self.ptc is not None:
            result['ptc'] = self.ptc

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.baggage_sub_content_visualizes = []
        if m.get('baggage_sub_content_visualizes') is not None:
            for k1 in m.get('baggage_sub_content_visualizes'):
                temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListBaggageItemBaggageSubItemsBaggageSubContentVisualizes()
                self.baggage_sub_content_visualizes.append(temp_model.from_map(k1))

        if m.get('extra_content_visualizes') is not None:
            self.extra_content_visualizes = m.get('extra_content_visualizes')

        if m.get('is_struct') is not None:
            self.is_struct = m.get('is_struct')

        if m.get('ptc') is not None:
            self.ptc = m.get('ptc')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListBaggageItemBaggageSubItemsBaggageSubContentVisualizes(DaraModel):
    def __init__(
        self,
        baggage_desc: List[str] = None,
        baggage_sub_content_type: int = None,
        description: main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListBaggageItemBaggageSubItemsBaggageSubContentVisualizesDescription = None,
        image_do: main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListBaggageItemBaggageSubItemsBaggageSubContentVisualizesImageDO = None,
        is_highlight: bool = None,
        sub_title: str = None,
    ):
        self.baggage_desc = baggage_desc
        self.baggage_sub_content_type = baggage_sub_content_type
        self.description = description
        self.image_do = image_do
        self.is_highlight = is_highlight
        self.sub_title = sub_title

    def validate(self):
        if self.description:
            self.description.validate()
        if self.image_do:
            self.image_do.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baggage_desc is not None:
            result['baggage_desc'] = self.baggage_desc

        if self.baggage_sub_content_type is not None:
            result['baggage_sub_content_type'] = self.baggage_sub_content_type

        if self.description is not None:
            result['description'] = self.description.to_map()

        if self.image_do is not None:
            result['image_d_o'] = self.image_do.to_map()

        if self.is_highlight is not None:
            result['is_highlight'] = self.is_highlight

        if self.sub_title is not None:
            result['sub_title'] = self.sub_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baggage_desc') is not None:
            self.baggage_desc = m.get('baggage_desc')

        if m.get('baggage_sub_content_type') is not None:
            self.baggage_sub_content_type = m.get('baggage_sub_content_type')

        if m.get('description') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListBaggageItemBaggageSubItemsBaggageSubContentVisualizesDescription()
            self.description = temp_model.from_map(m.get('description'))

        if m.get('image_d_o') is not None:
            temp_model = main_models.FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListBaggageItemBaggageSubItemsBaggageSubContentVisualizesImageDO()
            self.image_do = temp_model.from_map(m.get('image_d_o'))

        if m.get('is_highlight') is not None:
            self.is_highlight = m.get('is_highlight')

        if m.get('sub_title') is not None:
            self.sub_title = m.get('sub_title')

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListBaggageItemBaggageSubItemsBaggageSubContentVisualizesImageDO(DaraModel):
    def __init__(
        self,
        image: str = None,
        largest: str = None,
        middle: str = None,
        smallest: str = None,
    ):
        self.image = image
        self.largest = largest
        self.middle = middle
        self.smallest = smallest

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image is not None:
            result['image'] = self.image

        if self.largest is not None:
            result['largest'] = self.largest

        if self.middle is not None:
            result['middle'] = self.middle

        if self.smallest is not None:
            result['smallest'] = self.smallest

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('largest') is not None:
            self.largest = m.get('largest')

        if m.get('middle') is not None:
            self.middle = m.get('middle')

        if m.get('smallest') is not None:
            self.smallest = m.get('smallest')

        return self

class FlightOtaSearchResponseBodyModuleFlightListCabinInfoListFlightRuleListBaggageItemBaggageSubItemsBaggageSubContentVisualizesDescription(DaraModel):
    def __init__(
        self,
        desc: str = None,
        icon: str = None,
        image: str = None,
        title: str = None,
    ):
        self.desc = desc
        self.icon = icon
        self.image = image
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['desc'] = self.desc

        if self.icon is not None:
            result['icon'] = self.icon

        if self.image is not None:
            result['image'] = self.image

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('icon') is not None:
            self.icon = m.get('icon')

        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaSearchResponseBodyModuleFlightListArrAirportInfo(DaraModel):
    def __init__(
        self,
        airport_code: str = None,
        airport_name: str = None,
        city_code: str = None,
        city_name: str = None,
        terminal: str = None,
    ):
        self.airport_code = airport_code
        self.airport_name = airport_name
        self.city_code = city_code
        self.city_name = city_name
        self.terminal = terminal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airport_code is not None:
            result['airport_code'] = self.airport_code

        if self.airport_name is not None:
            result['airport_name'] = self.airport_name

        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.city_name is not None:
            result['city_name'] = self.city_name

        if self.terminal is not None:
            result['terminal'] = self.terminal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airport_code') is not None:
            self.airport_code = m.get('airport_code')

        if m.get('airport_name') is not None:
            self.airport_name = m.get('airport_name')

        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')

        if m.get('terminal') is not None:
            self.terminal = m.get('terminal')

        return self

class FlightOtaSearchResponseBodyModuleFlightListAirlineInfo(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        airline_name: str = None,
        airline_simple_name: str = None,
    ):
        self.airline_code = airline_code
        self.airline_name = airline_name
        self.airline_simple_name = airline_simple_name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_name') is not None:
            self.airline_name = m.get('airline_name')

        if m.get('airline_simple_name') is not None:
            self.airline_simple_name = m.get('airline_simple_name')

        return self

