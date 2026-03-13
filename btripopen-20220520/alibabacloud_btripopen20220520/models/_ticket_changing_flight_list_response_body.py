# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TicketChangingFlightListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.TicketChangingFlightListResponseBodyModule = None,
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
            temp_model = main_models.TicketChangingFlightListResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class TicketChangingFlightListResponseBodyModule(DaraModel):
    def __init__(
        self,
        flight_info_list: List[main_models.TicketChangingFlightListResponseBodyModuleFlightInfoList] = None,
    ):
        self.flight_info_list = flight_info_list

    def validate(self):
        if self.flight_info_list:
            for v1 in self.flight_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['flight_info_list'] = []
        if self.flight_info_list is not None:
            for k1 in self.flight_info_list:
                result['flight_info_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flight_info_list = []
        if m.get('flight_info_list') is not None:
            for k1 in m.get('flight_info_list'):
                temp_model = main_models.TicketChangingFlightListResponseBodyModuleFlightInfoList()
                self.flight_info_list.append(temp_model.from_map(k1))

        return self

class TicketChangingFlightListResponseBodyModuleFlightInfoList(DaraModel):
    def __init__(
        self,
        airline_info: main_models.TicketChangingFlightListResponseBodyModuleFlightInfoListAirlineInfo = None,
        arr_airport_info: main_models.TicketChangingFlightListResponseBodyModuleFlightInfoListArrAirportInfo = None,
        cabin_list: List[main_models.TicketChangingFlightListResponseBodyModuleFlightInfoListCabinList] = None,
        carrier_airline: str = None,
        carrier_no: str = None,
        dep_airport_info: main_models.TicketChangingFlightListResponseBodyModuleFlightInfoListDepAirportInfo = None,
        flight_no: str = None,
        flight_size: str = None,
        flight_type: str = None,
        is_protocol: bool = None,
        is_share: bool = None,
        is_stop: bool = None,
        lowest_cabin: str = None,
        lowest_cabin_class: str = None,
        lowest_cabin_desc: str = None,
        lowest_cabin_num: str = None,
        lowest_cabin_price: List[main_models.TicketChangingFlightListResponseBodyModuleFlightInfoListLowestCabinPrice] = None,
        meal_desc: str = None,
        modify_flight_arr_time: str = None,
        modify_flight_dep_date: str = None,
        modify_flight_dep_time: str = None,
        session_id: str = None,
        stop_arr_time: str = None,
        stop_city: str = None,
        stop_dep_time: str = None,
    ):
        self.airline_info = airline_info
        self.arr_airport_info = arr_airport_info
        self.cabin_list = cabin_list
        self.carrier_airline = carrier_airline
        self.carrier_no = carrier_no
        self.dep_airport_info = dep_airport_info
        self.flight_no = flight_no
        self.flight_size = flight_size
        self.flight_type = flight_type
        self.is_protocol = is_protocol
        self.is_share = is_share
        self.is_stop = is_stop
        self.lowest_cabin = lowest_cabin
        self.lowest_cabin_class = lowest_cabin_class
        self.lowest_cabin_desc = lowest_cabin_desc
        self.lowest_cabin_num = lowest_cabin_num
        self.lowest_cabin_price = lowest_cabin_price
        self.meal_desc = meal_desc
        self.modify_flight_arr_time = modify_flight_arr_time
        self.modify_flight_dep_date = modify_flight_dep_date
        self.modify_flight_dep_time = modify_flight_dep_time
        self.session_id = session_id
        self.stop_arr_time = stop_arr_time
        self.stop_city = stop_city
        self.stop_dep_time = stop_dep_time

    def validate(self):
        if self.airline_info:
            self.airline_info.validate()
        if self.arr_airport_info:
            self.arr_airport_info.validate()
        if self.cabin_list:
            for v1 in self.cabin_list:
                 if v1:
                    v1.validate()
        if self.dep_airport_info:
            self.dep_airport_info.validate()
        if self.lowest_cabin_price:
            for v1 in self.lowest_cabin_price:
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

        result['cabin_list'] = []
        if self.cabin_list is not None:
            for k1 in self.cabin_list:
                result['cabin_list'].append(k1.to_map() if k1 else None)

        if self.carrier_airline is not None:
            result['carrier_airline'] = self.carrier_airline

        if self.carrier_no is not None:
            result['carrier_no'] = self.carrier_no

        if self.dep_airport_info is not None:
            result['dep_airport_info'] = self.dep_airport_info.to_map()

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.flight_size is not None:
            result['flight_size'] = self.flight_size

        if self.flight_type is not None:
            result['flight_type'] = self.flight_type

        if self.is_protocol is not None:
            result['is_protocol'] = self.is_protocol

        if self.is_share is not None:
            result['is_share'] = self.is_share

        if self.is_stop is not None:
            result['is_stop'] = self.is_stop

        if self.lowest_cabin is not None:
            result['lowest_cabin'] = self.lowest_cabin

        if self.lowest_cabin_class is not None:
            result['lowest_cabin_class'] = self.lowest_cabin_class

        if self.lowest_cabin_desc is not None:
            result['lowest_cabin_desc'] = self.lowest_cabin_desc

        if self.lowest_cabin_num is not None:
            result['lowest_cabin_num'] = self.lowest_cabin_num

        result['lowest_cabin_price'] = []
        if self.lowest_cabin_price is not None:
            for k1 in self.lowest_cabin_price:
                result['lowest_cabin_price'].append(k1.to_map() if k1 else None)

        if self.meal_desc is not None:
            result['meal_desc'] = self.meal_desc

        if self.modify_flight_arr_time is not None:
            result['modify_flight_arr_time'] = self.modify_flight_arr_time

        if self.modify_flight_dep_date is not None:
            result['modify_flight_dep_date'] = self.modify_flight_dep_date

        if self.modify_flight_dep_time is not None:
            result['modify_flight_dep_time'] = self.modify_flight_dep_time

        if self.session_id is not None:
            result['session_id'] = self.session_id

        if self.stop_arr_time is not None:
            result['stop_arr_time'] = self.stop_arr_time

        if self.stop_city is not None:
            result['stop_city'] = self.stop_city

        if self.stop_dep_time is not None:
            result['stop_dep_time'] = self.stop_dep_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_info') is not None:
            temp_model = main_models.TicketChangingFlightListResponseBodyModuleFlightInfoListAirlineInfo()
            self.airline_info = temp_model.from_map(m.get('airline_info'))

        if m.get('arr_airport_info') is not None:
            temp_model = main_models.TicketChangingFlightListResponseBodyModuleFlightInfoListArrAirportInfo()
            self.arr_airport_info = temp_model.from_map(m.get('arr_airport_info'))

        self.cabin_list = []
        if m.get('cabin_list') is not None:
            for k1 in m.get('cabin_list'):
                temp_model = main_models.TicketChangingFlightListResponseBodyModuleFlightInfoListCabinList()
                self.cabin_list.append(temp_model.from_map(k1))

        if m.get('carrier_airline') is not None:
            self.carrier_airline = m.get('carrier_airline')

        if m.get('carrier_no') is not None:
            self.carrier_no = m.get('carrier_no')

        if m.get('dep_airport_info') is not None:
            temp_model = main_models.TicketChangingFlightListResponseBodyModuleFlightInfoListDepAirportInfo()
            self.dep_airport_info = temp_model.from_map(m.get('dep_airport_info'))

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('flight_size') is not None:
            self.flight_size = m.get('flight_size')

        if m.get('flight_type') is not None:
            self.flight_type = m.get('flight_type')

        if m.get('is_protocol') is not None:
            self.is_protocol = m.get('is_protocol')

        if m.get('is_share') is not None:
            self.is_share = m.get('is_share')

        if m.get('is_stop') is not None:
            self.is_stop = m.get('is_stop')

        if m.get('lowest_cabin') is not None:
            self.lowest_cabin = m.get('lowest_cabin')

        if m.get('lowest_cabin_class') is not None:
            self.lowest_cabin_class = m.get('lowest_cabin_class')

        if m.get('lowest_cabin_desc') is not None:
            self.lowest_cabin_desc = m.get('lowest_cabin_desc')

        if m.get('lowest_cabin_num') is not None:
            self.lowest_cabin_num = m.get('lowest_cabin_num')

        self.lowest_cabin_price = []
        if m.get('lowest_cabin_price') is not None:
            for k1 in m.get('lowest_cabin_price'):
                temp_model = main_models.TicketChangingFlightListResponseBodyModuleFlightInfoListLowestCabinPrice()
                self.lowest_cabin_price.append(temp_model.from_map(k1))

        if m.get('meal_desc') is not None:
            self.meal_desc = m.get('meal_desc')

        if m.get('modify_flight_arr_time') is not None:
            self.modify_flight_arr_time = m.get('modify_flight_arr_time')

        if m.get('modify_flight_dep_date') is not None:
            self.modify_flight_dep_date = m.get('modify_flight_dep_date')

        if m.get('modify_flight_dep_time') is not None:
            self.modify_flight_dep_time = m.get('modify_flight_dep_time')

        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')

        if m.get('stop_arr_time') is not None:
            self.stop_arr_time = m.get('stop_arr_time')

        if m.get('stop_city') is not None:
            self.stop_city = m.get('stop_city')

        if m.get('stop_dep_time') is not None:
            self.stop_dep_time = m.get('stop_dep_time')

        return self

class TicketChangingFlightListResponseBodyModuleFlightInfoListLowestCabinPrice(DaraModel):
    def __init__(
        self,
        passenger_type: int = None,
        ticket_price: int = None,
        upgrade_fee: int = None,
        upgrade_price: int = None,
    ):
        self.passenger_type = passenger_type
        self.ticket_price = ticket_price
        self.upgrade_fee = upgrade_fee
        self.upgrade_price = upgrade_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.passenger_type is not None:
            result['passenger_type'] = self.passenger_type

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        if self.upgrade_fee is not None:
            result['upgrade_fee'] = self.upgrade_fee

        if self.upgrade_price is not None:
            result['upgrade_price'] = self.upgrade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passenger_type') is not None:
            self.passenger_type = m.get('passenger_type')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        if m.get('upgrade_fee') is not None:
            self.upgrade_fee = m.get('upgrade_fee')

        if m.get('upgrade_price') is not None:
            self.upgrade_price = m.get('upgrade_price')

        return self

class TicketChangingFlightListResponseBodyModuleFlightInfoListDepAirportInfo(DaraModel):
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

class TicketChangingFlightListResponseBodyModuleFlightInfoListCabinList(DaraModel):
    def __init__(
        self,
        cabin: str = None,
        cabin_class: str = None,
        cabin_desc: str = None,
        cabin_discount: int = None,
        child_cabin: str = None,
        left_num: str = None,
        modify_price_list: List[main_models.TicketChangingFlightListResponseBodyModuleFlightInfoListCabinListModifyPriceList] = None,
        ota_itemid: str = None,
    ):
        self.cabin = cabin
        self.cabin_class = cabin_class
        self.cabin_desc = cabin_desc
        self.cabin_discount = cabin_discount
        self.child_cabin = child_cabin
        self.left_num = left_num
        self.modify_price_list = modify_price_list
        self.ota_itemid = ota_itemid

    def validate(self):
        if self.modify_price_list:
            for v1 in self.modify_price_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cabin is not None:
            result['cabin'] = self.cabin

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.cabin_desc is not None:
            result['cabin_desc'] = self.cabin_desc

        if self.cabin_discount is not None:
            result['cabin_discount'] = self.cabin_discount

        if self.child_cabin is not None:
            result['child_cabin'] = self.child_cabin

        if self.left_num is not None:
            result['left_num'] = self.left_num

        result['modify_price_list'] = []
        if self.modify_price_list is not None:
            for k1 in self.modify_price_list:
                result['modify_price_list'].append(k1.to_map() if k1 else None)

        if self.ota_itemid is not None:
            result['ota_itemid'] = self.ota_itemid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('cabin_desc') is not None:
            self.cabin_desc = m.get('cabin_desc')

        if m.get('cabin_discount') is not None:
            self.cabin_discount = m.get('cabin_discount')

        if m.get('child_cabin') is not None:
            self.child_cabin = m.get('child_cabin')

        if m.get('left_num') is not None:
            self.left_num = m.get('left_num')

        self.modify_price_list = []
        if m.get('modify_price_list') is not None:
            for k1 in m.get('modify_price_list'):
                temp_model = main_models.TicketChangingFlightListResponseBodyModuleFlightInfoListCabinListModifyPriceList()
                self.modify_price_list.append(temp_model.from_map(k1))

        if m.get('ota_itemid') is not None:
            self.ota_itemid = m.get('ota_itemid')

        return self

class TicketChangingFlightListResponseBodyModuleFlightInfoListCabinListModifyPriceList(DaraModel):
    def __init__(
        self,
        passenger_type: int = None,
        ticket_price: int = None,
        upgrade_fee: int = None,
        upgrade_price: int = None,
    ):
        self.passenger_type = passenger_type
        self.ticket_price = ticket_price
        self.upgrade_fee = upgrade_fee
        self.upgrade_price = upgrade_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.passenger_type is not None:
            result['passenger_type'] = self.passenger_type

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        if self.upgrade_fee is not None:
            result['upgrade_fee'] = self.upgrade_fee

        if self.upgrade_price is not None:
            result['upgrade_price'] = self.upgrade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passenger_type') is not None:
            self.passenger_type = m.get('passenger_type')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        if m.get('upgrade_fee') is not None:
            self.upgrade_fee = m.get('upgrade_fee')

        if m.get('upgrade_price') is not None:
            self.upgrade_price = m.get('upgrade_price')

        return self

class TicketChangingFlightListResponseBodyModuleFlightInfoListArrAirportInfo(DaraModel):
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

class TicketChangingFlightListResponseBodyModuleFlightInfoListAirlineInfo(DaraModel):
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

