# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightModifyListingSearchV2ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.FlightModifyListingSearchV2ResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        # module
        self.module = module
        # requestId
        self.request_id = request_id
        self.success = success
        # requestId
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
            temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class FlightModifyListingSearchV2ResponseBodyModule(DaraModel):
    def __init__(
        self,
        direct_flight_list: List[main_models.FlightModifyListingSearchV2ResponseBodyModuleDirectFlightList] = None,
        next_req_wait_time: int = None,
        retry: bool = None,
        search_retry_token: str = None,
        session_id: str = None,
        transfer_flight_list: List[main_models.FlightModifyListingSearchV2ResponseBodyModuleTransferFlightList] = None,
        transfer_title: str = None,
    ):
        self.direct_flight_list = direct_flight_list
        self.next_req_wait_time = next_req_wait_time
        self.retry = retry
        self.search_retry_token = search_retry_token
        self.session_id = session_id
        self.transfer_flight_list = transfer_flight_list
        self.transfer_title = transfer_title

    def validate(self):
        if self.direct_flight_list:
            for v1 in self.direct_flight_list:
                 if v1:
                    v1.validate()
        if self.transfer_flight_list:
            for v1 in self.transfer_flight_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['direct_flight_list'] = []
        if self.direct_flight_list is not None:
            for k1 in self.direct_flight_list:
                result['direct_flight_list'].append(k1.to_map() if k1 else None)

        if self.next_req_wait_time is not None:
            result['next_req_wait_time'] = self.next_req_wait_time

        if self.retry is not None:
            result['retry'] = self.retry

        if self.search_retry_token is not None:
            result['search_retry_token'] = self.search_retry_token

        if self.session_id is not None:
            result['session_id'] = self.session_id

        result['transfer_flight_list'] = []
        if self.transfer_flight_list is not None:
            for k1 in self.transfer_flight_list:
                result['transfer_flight_list'].append(k1.to_map() if k1 else None)

        if self.transfer_title is not None:
            result['transfer_title'] = self.transfer_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.direct_flight_list = []
        if m.get('direct_flight_list') is not None:
            for k1 in m.get('direct_flight_list'):
                temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModuleDirectFlightList()
                self.direct_flight_list.append(temp_model.from_map(k1))

        if m.get('next_req_wait_time') is not None:
            self.next_req_wait_time = m.get('next_req_wait_time')

        if m.get('retry') is not None:
            self.retry = m.get('retry')

        if m.get('search_retry_token') is not None:
            self.search_retry_token = m.get('search_retry_token')

        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')

        self.transfer_flight_list = []
        if m.get('transfer_flight_list') is not None:
            for k1 in m.get('transfer_flight_list'):
                temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModuleTransferFlightList()
                self.transfer_flight_list.append(temp_model.from_map(k1))

        if m.get('transfer_title') is not None:
            self.transfer_title = m.get('transfer_title')

        return self

class FlightModifyListingSearchV2ResponseBodyModuleTransferFlightList(DaraModel):
    def __init__(
        self,
        airline_info: main_models.FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListAirlineInfo = None,
        arr_airport_info: main_models.FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListArrAirportInfo = None,
        arr_city_code: str = None,
        arr_time: str = None,
        cabin_class: str = None,
        cabin_class_name: str = None,
        dep_airport_info: main_models.FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListDepAirportInfo = None,
        dep_city_code: str = None,
        dep_time: str = None,
        duration: int = None,
        flight_no: str = None,
        flight_share_info: main_models.FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListFlightShareInfo = None,
        flight_size: str = None,
        flight_stop_info: main_models.FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListFlightStopInfo = None,
        flight_transfer_info: main_models.FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListFlightTransferInfo = None,
        flight_type: str = None,
        journey_seq: int = None,
        left_num: str = None,
        manufacturer: str = None,
        meal_desc: str = None,
        price_info_dto: main_models.FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListPriceInfoDTO = None,
        segment_seq: int = None,
        share: bool = None,
        short_flight_size: str = None,
        span_day: str = None,
        stop: bool = None,
        transfer: bool = None,
    ):
        self.airline_info = airline_info
        self.arr_airport_info = arr_airport_info
        self.arr_city_code = arr_city_code
        self.arr_time = arr_time
        self.cabin_class = cabin_class
        self.cabin_class_name = cabin_class_name
        self.dep_airport_info = dep_airport_info
        self.dep_city_code = dep_city_code
        self.dep_time = dep_time
        self.duration = duration
        self.flight_no = flight_no
        self.flight_share_info = flight_share_info
        self.flight_size = flight_size
        self.flight_stop_info = flight_stop_info
        self.flight_transfer_info = flight_transfer_info
        self.flight_type = flight_type
        self.journey_seq = journey_seq
        self.left_num = left_num
        self.manufacturer = manufacturer
        self.meal_desc = meal_desc
        self.price_info_dto = price_info_dto
        self.segment_seq = segment_seq
        self.share = share
        self.short_flight_size = short_flight_size
        self.span_day = span_day
        self.stop = stop
        self.transfer = transfer

    def validate(self):
        if self.airline_info:
            self.airline_info.validate()
        if self.arr_airport_info:
            self.arr_airport_info.validate()
        if self.dep_airport_info:
            self.dep_airport_info.validate()
        if self.flight_share_info:
            self.flight_share_info.validate()
        if self.flight_stop_info:
            self.flight_stop_info.validate()
        if self.flight_transfer_info:
            self.flight_transfer_info.validate()
        if self.price_info_dto:
            self.price_info_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_info is not None:
            result['airline_info'] = self.airline_info.to_map()

        if self.arr_airport_info is not None:
            result['arr_airport_info'] = self.arr_airport_info.to_map()

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.cabin_class is not None:
            result['cabinClass'] = self.cabin_class

        if self.cabin_class_name is not None:
            result['cabinClassName'] = self.cabin_class_name

        if self.dep_airport_info is not None:
            result['dep_airport_info'] = self.dep_airport_info.to_map()

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.duration is not None:
            result['duration'] = self.duration

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.flight_share_info is not None:
            result['flight_share_info'] = self.flight_share_info.to_map()

        if self.flight_size is not None:
            result['flight_size'] = self.flight_size

        if self.flight_stop_info is not None:
            result['flight_stop_info'] = self.flight_stop_info.to_map()

        if self.flight_transfer_info is not None:
            result['flight_transfer_info'] = self.flight_transfer_info.to_map()

        if self.flight_type is not None:
            result['flight_type'] = self.flight_type

        if self.journey_seq is not None:
            result['journey_seq'] = self.journey_seq

        if self.left_num is not None:
            result['left_num'] = self.left_num

        if self.manufacturer is not None:
            result['manufacturer'] = self.manufacturer

        if self.meal_desc is not None:
            result['meal_desc'] = self.meal_desc

        if self.price_info_dto is not None:
            result['price_info_d_t_o'] = self.price_info_dto.to_map()

        if self.segment_seq is not None:
            result['segment_seq'] = self.segment_seq

        if self.share is not None:
            result['share'] = self.share

        if self.short_flight_size is not None:
            result['short_flight_size'] = self.short_flight_size

        if self.span_day is not None:
            result['span_day'] = self.span_day

        if self.stop is not None:
            result['stop'] = self.stop

        if self.transfer is not None:
            result['transfer'] = self.transfer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_info') is not None:
            temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListAirlineInfo()
            self.airline_info = temp_model.from_map(m.get('airline_info'))

        if m.get('arr_airport_info') is not None:
            temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListArrAirportInfo()
            self.arr_airport_info = temp_model.from_map(m.get('arr_airport_info'))

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('cabinClass') is not None:
            self.cabin_class = m.get('cabinClass')

        if m.get('cabinClassName') is not None:
            self.cabin_class_name = m.get('cabinClassName')

        if m.get('dep_airport_info') is not None:
            temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListDepAirportInfo()
            self.dep_airport_info = temp_model.from_map(m.get('dep_airport_info'))

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('flight_share_info') is not None:
            temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListFlightShareInfo()
            self.flight_share_info = temp_model.from_map(m.get('flight_share_info'))

        if m.get('flight_size') is not None:
            self.flight_size = m.get('flight_size')

        if m.get('flight_stop_info') is not None:
            temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListFlightStopInfo()
            self.flight_stop_info = temp_model.from_map(m.get('flight_stop_info'))

        if m.get('flight_transfer_info') is not None:
            temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListFlightTransferInfo()
            self.flight_transfer_info = temp_model.from_map(m.get('flight_transfer_info'))

        if m.get('flight_type') is not None:
            self.flight_type = m.get('flight_type')

        if m.get('journey_seq') is not None:
            self.journey_seq = m.get('journey_seq')

        if m.get('left_num') is not None:
            self.left_num = m.get('left_num')

        if m.get('manufacturer') is not None:
            self.manufacturer = m.get('manufacturer')

        if m.get('meal_desc') is not None:
            self.meal_desc = m.get('meal_desc')

        if m.get('price_info_d_t_o') is not None:
            temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListPriceInfoDTO()
            self.price_info_dto = temp_model.from_map(m.get('price_info_d_t_o'))

        if m.get('segment_seq') is not None:
            self.segment_seq = m.get('segment_seq')

        if m.get('share') is not None:
            self.share = m.get('share')

        if m.get('short_flight_size') is not None:
            self.short_flight_size = m.get('short_flight_size')

        if m.get('span_day') is not None:
            self.span_day = m.get('span_day')

        if m.get('stop') is not None:
            self.stop = m.get('stop')

        if m.get('transfer') is not None:
            self.transfer = m.get('transfer')

        return self

class FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListPriceInfoDTO(DaraModel):
    def __init__(
        self,
        adult_price: int = None,
        adult_tax: int = None,
        adult_total_price: int = None,
        before_control_price: int = None,
        child_price: int = None,
        child_tax: int = None,
        child_total_price: int = None,
        infant_price: int = None,
        infant_tax: int = None,
        infant_total_price: int = None,
        original_adult_price: int = None,
        original_adult_total_price: int = None,
        re_shop_price_info_dto: main_models.FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListPriceInfoDTOReShopPriceInfoDTO = None,
    ):
        self.adult_price = adult_price
        self.adult_tax = adult_tax
        self.adult_total_price = adult_total_price
        self.before_control_price = before_control_price
        self.child_price = child_price
        self.child_tax = child_tax
        self.child_total_price = child_total_price
        self.infant_price = infant_price
        self.infant_tax = infant_tax
        self.infant_total_price = infant_total_price
        self.original_adult_price = original_adult_price
        self.original_adult_total_price = original_adult_total_price
        self.re_shop_price_info_dto = re_shop_price_info_dto

    def validate(self):
        if self.re_shop_price_info_dto:
            self.re_shop_price_info_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adult_price is not None:
            result['adult_price'] = self.adult_price

        if self.adult_tax is not None:
            result['adult_tax'] = self.adult_tax

        if self.adult_total_price is not None:
            result['adult_total_price'] = self.adult_total_price

        if self.before_control_price is not None:
            result['before_control_price'] = self.before_control_price

        if self.child_price is not None:
            result['child_price'] = self.child_price

        if self.child_tax is not None:
            result['child_tax'] = self.child_tax

        if self.child_total_price is not None:
            result['child_total_price'] = self.child_total_price

        if self.infant_price is not None:
            result['infant_price'] = self.infant_price

        if self.infant_tax is not None:
            result['infant_tax'] = self.infant_tax

        if self.infant_total_price is not None:
            result['infant_total_price'] = self.infant_total_price

        if self.original_adult_price is not None:
            result['original_adult_price'] = self.original_adult_price

        if self.original_adult_total_price is not None:
            result['original_adult_total_price'] = self.original_adult_total_price

        if self.re_shop_price_info_dto is not None:
            result['re_shop_price_info_d_t_o'] = self.re_shop_price_info_dto.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adult_price') is not None:
            self.adult_price = m.get('adult_price')

        if m.get('adult_tax') is not None:
            self.adult_tax = m.get('adult_tax')

        if m.get('adult_total_price') is not None:
            self.adult_total_price = m.get('adult_total_price')

        if m.get('before_control_price') is not None:
            self.before_control_price = m.get('before_control_price')

        if m.get('child_price') is not None:
            self.child_price = m.get('child_price')

        if m.get('child_tax') is not None:
            self.child_tax = m.get('child_tax')

        if m.get('child_total_price') is not None:
            self.child_total_price = m.get('child_total_price')

        if m.get('infant_price') is not None:
            self.infant_price = m.get('infant_price')

        if m.get('infant_tax') is not None:
            self.infant_tax = m.get('infant_tax')

        if m.get('infant_total_price') is not None:
            self.infant_total_price = m.get('infant_total_price')

        if m.get('original_adult_price') is not None:
            self.original_adult_price = m.get('original_adult_price')

        if m.get('original_adult_total_price') is not None:
            self.original_adult_total_price = m.get('original_adult_total_price')

        if m.get('re_shop_price_info_d_t_o') is not None:
            temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListPriceInfoDTOReShopPriceInfoDTO()
            self.re_shop_price_info_dto = temp_model.from_map(m.get('re_shop_price_info_d_t_o'))

        return self

class FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListPriceInfoDTOReShopPriceInfoDTO(DaraModel):
    def __init__(
        self,
        re_shop_adult_change_fee: int = None,
        re_shop_adult_price: int = None,
        re_shop_adult_price_gap: int = None,
        re_shop_child_change_fee: int = None,
        re_shop_child_price: int = None,
        re_shop_child_price_gap: int = None,
        re_shop_inf_change_fee: int = None,
        re_shop_inf_price: int = None,
        re_shop_inf_price_gap: int = None,
    ):
        self.re_shop_adult_change_fee = re_shop_adult_change_fee
        self.re_shop_adult_price = re_shop_adult_price
        self.re_shop_adult_price_gap = re_shop_adult_price_gap
        self.re_shop_child_change_fee = re_shop_child_change_fee
        self.re_shop_child_price = re_shop_child_price
        self.re_shop_child_price_gap = re_shop_child_price_gap
        self.re_shop_inf_change_fee = re_shop_inf_change_fee
        self.re_shop_inf_price = re_shop_inf_price
        self.re_shop_inf_price_gap = re_shop_inf_price_gap

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.re_shop_adult_change_fee is not None:
            result['re_shop_adult_change_fee'] = self.re_shop_adult_change_fee

        if self.re_shop_adult_price is not None:
            result['re_shop_adult_price'] = self.re_shop_adult_price

        if self.re_shop_adult_price_gap is not None:
            result['re_shop_adult_price_gap'] = self.re_shop_adult_price_gap

        if self.re_shop_child_change_fee is not None:
            result['re_shop_child_change_fee'] = self.re_shop_child_change_fee

        if self.re_shop_child_price is not None:
            result['re_shop_child_price'] = self.re_shop_child_price

        if self.re_shop_child_price_gap is not None:
            result['re_shop_child_price_gap'] = self.re_shop_child_price_gap

        if self.re_shop_inf_change_fee is not None:
            result['re_shop_inf_change_fee'] = self.re_shop_inf_change_fee

        if self.re_shop_inf_price is not None:
            result['re_shop_inf_price'] = self.re_shop_inf_price

        if self.re_shop_inf_price_gap is not None:
            result['re_shop_inf_price_gap'] = self.re_shop_inf_price_gap

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('re_shop_adult_change_fee') is not None:
            self.re_shop_adult_change_fee = m.get('re_shop_adult_change_fee')

        if m.get('re_shop_adult_price') is not None:
            self.re_shop_adult_price = m.get('re_shop_adult_price')

        if m.get('re_shop_adult_price_gap') is not None:
            self.re_shop_adult_price_gap = m.get('re_shop_adult_price_gap')

        if m.get('re_shop_child_change_fee') is not None:
            self.re_shop_child_change_fee = m.get('re_shop_child_change_fee')

        if m.get('re_shop_child_price') is not None:
            self.re_shop_child_price = m.get('re_shop_child_price')

        if m.get('re_shop_child_price_gap') is not None:
            self.re_shop_child_price_gap = m.get('re_shop_child_price_gap')

        if m.get('re_shop_inf_change_fee') is not None:
            self.re_shop_inf_change_fee = m.get('re_shop_inf_change_fee')

        if m.get('re_shop_inf_price') is not None:
            self.re_shop_inf_price = m.get('re_shop_inf_price')

        if m.get('re_shop_inf_price_gap') is not None:
            self.re_shop_inf_price_gap = m.get('re_shop_inf_price_gap')

        return self

class FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListFlightTransferInfo(DaraModel):
    def __init__(
        self,
        transfer_airline_info: main_models.FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListFlightTransferInfoTransferAirlineInfo = None,
        transfer_city_code: str = None,
        transfer_city_name: str = None,
        transfer_dep_time: str = None,
        transfer_flight_no: str = None,
        transfer_flight_size: str = None,
        transfer_share: bool = None,
        transfer_stop_time: int = None,
    ):
        self.transfer_airline_info = transfer_airline_info
        self.transfer_city_code = transfer_city_code
        self.transfer_city_name = transfer_city_name
        self.transfer_dep_time = transfer_dep_time
        self.transfer_flight_no = transfer_flight_no
        self.transfer_flight_size = transfer_flight_size
        self.transfer_share = transfer_share
        self.transfer_stop_time = transfer_stop_time

    def validate(self):
        if self.transfer_airline_info:
            self.transfer_airline_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.transfer_airline_info is not None:
            result['transfer_airline_info'] = self.transfer_airline_info.to_map()

        if self.transfer_city_code is not None:
            result['transfer_city_code'] = self.transfer_city_code

        if self.transfer_city_name is not None:
            result['transfer_city_name'] = self.transfer_city_name

        if self.transfer_dep_time is not None:
            result['transfer_dep_time'] = self.transfer_dep_time

        if self.transfer_flight_no is not None:
            result['transfer_flight_no'] = self.transfer_flight_no

        if self.transfer_flight_size is not None:
            result['transfer_flight_size'] = self.transfer_flight_size

        if self.transfer_share is not None:
            result['transfer_share'] = self.transfer_share

        if self.transfer_stop_time is not None:
            result['transfer_stop_time'] = self.transfer_stop_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('transfer_airline_info') is not None:
            temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListFlightTransferInfoTransferAirlineInfo()
            self.transfer_airline_info = temp_model.from_map(m.get('transfer_airline_info'))

        if m.get('transfer_city_code') is not None:
            self.transfer_city_code = m.get('transfer_city_code')

        if m.get('transfer_city_name') is not None:
            self.transfer_city_name = m.get('transfer_city_name')

        if m.get('transfer_dep_time') is not None:
            self.transfer_dep_time = m.get('transfer_dep_time')

        if m.get('transfer_flight_no') is not None:
            self.transfer_flight_no = m.get('transfer_flight_no')

        if m.get('transfer_flight_size') is not None:
            self.transfer_flight_size = m.get('transfer_flight_size')

        if m.get('transfer_share') is not None:
            self.transfer_share = m.get('transfer_share')

        if m.get('transfer_stop_time') is not None:
            self.transfer_stop_time = m.get('transfer_stop_time')

        return self

class FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListFlightTransferInfoTransferAirlineInfo(DaraModel):
    def __init__(
        self,
        airline_chinese_name: str = None,
        airline_chinese_short_name: str = None,
        airline_code: str = None,
        airline_icon: str = None,
        cheap_flight: bool = None,
    ):
        self.airline_chinese_name = airline_chinese_name
        self.airline_chinese_short_name = airline_chinese_short_name
        self.airline_code = airline_code
        self.airline_icon = airline_icon
        self.cheap_flight = cheap_flight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_chinese_name is not None:
            result['airline_chinese_name'] = self.airline_chinese_name

        if self.airline_chinese_short_name is not None:
            result['airline_chinese_short_name'] = self.airline_chinese_short_name

        if self.airline_code is not None:
            result['airline_code'] = self.airline_code

        if self.airline_icon is not None:
            result['airline_icon'] = self.airline_icon

        if self.cheap_flight is not None:
            result['cheap_flight'] = self.cheap_flight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_chinese_name') is not None:
            self.airline_chinese_name = m.get('airline_chinese_name')

        if m.get('airline_chinese_short_name') is not None:
            self.airline_chinese_short_name = m.get('airline_chinese_short_name')

        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_icon') is not None:
            self.airline_icon = m.get('airline_icon')

        if m.get('cheap_flight') is not None:
            self.cheap_flight = m.get('cheap_flight')

        return self

class FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListFlightStopInfo(DaraModel):
    def __init__(
        self,
        stop_airport: str = None,
        stop_arr_term: str = None,
        stop_arr_time: str = None,
        stop_city_code: str = None,
        stop_city_name: str = None,
        stop_dep_term: str = None,
        stop_dep_time: str = None,
    ):
        self.stop_airport = stop_airport
        self.stop_arr_term = stop_arr_term
        self.stop_arr_time = stop_arr_time
        self.stop_city_code = stop_city_code
        self.stop_city_name = stop_city_name
        self.stop_dep_term = stop_dep_term
        self.stop_dep_time = stop_dep_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stop_airport is not None:
            result['stop_airport'] = self.stop_airport

        if self.stop_arr_term is not None:
            result['stop_arr_term'] = self.stop_arr_term

        if self.stop_arr_time is not None:
            result['stop_arr_time'] = self.stop_arr_time

        if self.stop_city_code is not None:
            result['stop_city_code'] = self.stop_city_code

        if self.stop_city_name is not None:
            result['stop_city_name'] = self.stop_city_name

        if self.stop_dep_term is not None:
            result['stop_dep_term'] = self.stop_dep_term

        if self.stop_dep_time is not None:
            result['stop_dep_time'] = self.stop_dep_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stop_airport') is not None:
            self.stop_airport = m.get('stop_airport')

        if m.get('stop_arr_term') is not None:
            self.stop_arr_term = m.get('stop_arr_term')

        if m.get('stop_arr_time') is not None:
            self.stop_arr_time = m.get('stop_arr_time')

        if m.get('stop_city_code') is not None:
            self.stop_city_code = m.get('stop_city_code')

        if m.get('stop_city_name') is not None:
            self.stop_city_name = m.get('stop_city_name')

        if m.get('stop_dep_term') is not None:
            self.stop_dep_term = m.get('stop_dep_term')

        if m.get('stop_dep_time') is not None:
            self.stop_dep_time = m.get('stop_dep_time')

        return self

class FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListFlightShareInfo(DaraModel):
    def __init__(
        self,
        operating_airline_info: main_models.FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListFlightShareInfoOperatingAirlineInfo = None,
        operating_flight_no: str = None,
    ):
        self.operating_airline_info = operating_airline_info
        self.operating_flight_no = operating_flight_no

    def validate(self):
        if self.operating_airline_info:
            self.operating_airline_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operating_airline_info is not None:
            result['operating_airline_info'] = self.operating_airline_info.to_map()

        if self.operating_flight_no is not None:
            result['operating_flight_no'] = self.operating_flight_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operating_airline_info') is not None:
            temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListFlightShareInfoOperatingAirlineInfo()
            self.operating_airline_info = temp_model.from_map(m.get('operating_airline_info'))

        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')

        return self

class FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListFlightShareInfoOperatingAirlineInfo(DaraModel):
    def __init__(
        self,
        airline_chinese_name: str = None,
        airline_chinese_short_name: str = None,
        airline_code: str = None,
        airline_icon: str = None,
        cheap_flight: bool = None,
    ):
        self.airline_chinese_name = airline_chinese_name
        self.airline_chinese_short_name = airline_chinese_short_name
        self.airline_code = airline_code
        self.airline_icon = airline_icon
        self.cheap_flight = cheap_flight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_chinese_name is not None:
            result['airline_chinese_name'] = self.airline_chinese_name

        if self.airline_chinese_short_name is not None:
            result['airline_chinese_short_name'] = self.airline_chinese_short_name

        if self.airline_code is not None:
            result['airline_code'] = self.airline_code

        if self.airline_icon is not None:
            result['airline_icon'] = self.airline_icon

        if self.cheap_flight is not None:
            result['cheap_flight'] = self.cheap_flight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_chinese_name') is not None:
            self.airline_chinese_name = m.get('airline_chinese_name')

        if m.get('airline_chinese_short_name') is not None:
            self.airline_chinese_short_name = m.get('airline_chinese_short_name')

        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_icon') is not None:
            self.airline_icon = m.get('airline_icon')

        if m.get('cheap_flight') is not None:
            self.cheap_flight = m.get('cheap_flight')

        return self

class FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListDepAirportInfo(DaraModel):
    def __init__(
        self,
        airport_code: str = None,
        airport_name: str = None,
        airport_short_name: str = None,
        terminal: str = None,
    ):
        self.airport_code = airport_code
        self.airport_name = airport_name
        self.airport_short_name = airport_short_name
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

        if self.airport_short_name is not None:
            result['airport_short_name'] = self.airport_short_name

        if self.terminal is not None:
            result['terminal'] = self.terminal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airport_code') is not None:
            self.airport_code = m.get('airport_code')

        if m.get('airport_name') is not None:
            self.airport_name = m.get('airport_name')

        if m.get('airport_short_name') is not None:
            self.airport_short_name = m.get('airport_short_name')

        if m.get('terminal') is not None:
            self.terminal = m.get('terminal')

        return self

class FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListArrAirportInfo(DaraModel):
    def __init__(
        self,
        airport_code: str = None,
        airport_name: str = None,
        airport_short_name: str = None,
        terminal: str = None,
    ):
        self.airport_code = airport_code
        self.airport_name = airport_name
        self.airport_short_name = airport_short_name
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

        if self.airport_short_name is not None:
            result['airport_short_name'] = self.airport_short_name

        if self.terminal is not None:
            result['terminal'] = self.terminal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airport_code') is not None:
            self.airport_code = m.get('airport_code')

        if m.get('airport_name') is not None:
            self.airport_name = m.get('airport_name')

        if m.get('airport_short_name') is not None:
            self.airport_short_name = m.get('airport_short_name')

        if m.get('terminal') is not None:
            self.terminal = m.get('terminal')

        return self

class FlightModifyListingSearchV2ResponseBodyModuleTransferFlightListAirlineInfo(DaraModel):
    def __init__(
        self,
        airline_chinese_name: str = None,
        airline_chinese_short_name: str = None,
        airline_code: str = None,
        airline_icon: str = None,
        cheap_flight: bool = None,
    ):
        self.airline_chinese_name = airline_chinese_name
        self.airline_chinese_short_name = airline_chinese_short_name
        self.airline_code = airline_code
        self.airline_icon = airline_icon
        self.cheap_flight = cheap_flight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_chinese_name is not None:
            result['airline_chinese_name'] = self.airline_chinese_name

        if self.airline_chinese_short_name is not None:
            result['airline_chinese_short_name'] = self.airline_chinese_short_name

        if self.airline_code is not None:
            result['airline_code'] = self.airline_code

        if self.airline_icon is not None:
            result['airline_icon'] = self.airline_icon

        if self.cheap_flight is not None:
            result['cheap_flight'] = self.cheap_flight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_chinese_name') is not None:
            self.airline_chinese_name = m.get('airline_chinese_name')

        if m.get('airline_chinese_short_name') is not None:
            self.airline_chinese_short_name = m.get('airline_chinese_short_name')

        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_icon') is not None:
            self.airline_icon = m.get('airline_icon')

        if m.get('cheap_flight') is not None:
            self.cheap_flight = m.get('cheap_flight')

        return self

class FlightModifyListingSearchV2ResponseBodyModuleDirectFlightList(DaraModel):
    def __init__(
        self,
        airline_info: main_models.FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListAirlineInfo = None,
        arr_airport_info: main_models.FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListArrAirportInfo = None,
        arr_city_code: str = None,
        arr_time: str = None,
        cabin_class: str = None,
        cabin_class_name: str = None,
        dep_airport_info: main_models.FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListDepAirportInfo = None,
        dep_city_code: str = None,
        dep_time: str = None,
        duration: int = None,
        flight_no: str = None,
        flight_share_info: main_models.FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListFlightShareInfo = None,
        flight_size: str = None,
        flight_stop_info: main_models.FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListFlightStopInfo = None,
        flight_transfer_info: main_models.FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListFlightTransferInfo = None,
        flight_type: str = None,
        journey_seq: int = None,
        left_num: str = None,
        manufacturer: str = None,
        meal_desc: str = None,
        price_info_dto: main_models.FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListPriceInfoDTO = None,
        segment_seq: int = None,
        share: bool = None,
        short_flight_size: str = None,
        span_day: str = None,
        stop: bool = None,
        transfer: bool = None,
    ):
        self.airline_info = airline_info
        self.arr_airport_info = arr_airport_info
        self.arr_city_code = arr_city_code
        self.arr_time = arr_time
        self.cabin_class = cabin_class
        self.cabin_class_name = cabin_class_name
        self.dep_airport_info = dep_airport_info
        self.dep_city_code = dep_city_code
        self.dep_time = dep_time
        self.duration = duration
        self.flight_no = flight_no
        self.flight_share_info = flight_share_info
        self.flight_size = flight_size
        self.flight_stop_info = flight_stop_info
        self.flight_transfer_info = flight_transfer_info
        self.flight_type = flight_type
        self.journey_seq = journey_seq
        self.left_num = left_num
        self.manufacturer = manufacturer
        self.meal_desc = meal_desc
        self.price_info_dto = price_info_dto
        self.segment_seq = segment_seq
        self.share = share
        self.short_flight_size = short_flight_size
        self.span_day = span_day
        self.stop = stop
        self.transfer = transfer

    def validate(self):
        if self.airline_info:
            self.airline_info.validate()
        if self.arr_airport_info:
            self.arr_airport_info.validate()
        if self.dep_airport_info:
            self.dep_airport_info.validate()
        if self.flight_share_info:
            self.flight_share_info.validate()
        if self.flight_stop_info:
            self.flight_stop_info.validate()
        if self.flight_transfer_info:
            self.flight_transfer_info.validate()
        if self.price_info_dto:
            self.price_info_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_info is not None:
            result['airline_info'] = self.airline_info.to_map()

        if self.arr_airport_info is not None:
            result['arr_airport_info'] = self.arr_airport_info.to_map()

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.cabin_class is not None:
            result['cabinClass'] = self.cabin_class

        if self.cabin_class_name is not None:
            result['cabinClassName'] = self.cabin_class_name

        if self.dep_airport_info is not None:
            result['dep_airport_info'] = self.dep_airport_info.to_map()

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.duration is not None:
            result['duration'] = self.duration

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.flight_share_info is not None:
            result['flight_share_info'] = self.flight_share_info.to_map()

        if self.flight_size is not None:
            result['flight_size'] = self.flight_size

        if self.flight_stop_info is not None:
            result['flight_stop_info'] = self.flight_stop_info.to_map()

        if self.flight_transfer_info is not None:
            result['flight_transfer_info'] = self.flight_transfer_info.to_map()

        if self.flight_type is not None:
            result['flight_type'] = self.flight_type

        if self.journey_seq is not None:
            result['journey_seq'] = self.journey_seq

        if self.left_num is not None:
            result['left_num'] = self.left_num

        if self.manufacturer is not None:
            result['manufacturer'] = self.manufacturer

        if self.meal_desc is not None:
            result['meal_desc'] = self.meal_desc

        if self.price_info_dto is not None:
            result['price_info_d_t_o'] = self.price_info_dto.to_map()

        if self.segment_seq is not None:
            result['segment_seq'] = self.segment_seq

        if self.share is not None:
            result['share'] = self.share

        if self.short_flight_size is not None:
            result['short_flight_size'] = self.short_flight_size

        if self.span_day is not None:
            result['span_day'] = self.span_day

        if self.stop is not None:
            result['stop'] = self.stop

        if self.transfer is not None:
            result['transfer'] = self.transfer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_info') is not None:
            temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListAirlineInfo()
            self.airline_info = temp_model.from_map(m.get('airline_info'))

        if m.get('arr_airport_info') is not None:
            temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListArrAirportInfo()
            self.arr_airport_info = temp_model.from_map(m.get('arr_airport_info'))

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('cabinClass') is not None:
            self.cabin_class = m.get('cabinClass')

        if m.get('cabinClassName') is not None:
            self.cabin_class_name = m.get('cabinClassName')

        if m.get('dep_airport_info') is not None:
            temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListDepAirportInfo()
            self.dep_airport_info = temp_model.from_map(m.get('dep_airport_info'))

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('flight_share_info') is not None:
            temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListFlightShareInfo()
            self.flight_share_info = temp_model.from_map(m.get('flight_share_info'))

        if m.get('flight_size') is not None:
            self.flight_size = m.get('flight_size')

        if m.get('flight_stop_info') is not None:
            temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListFlightStopInfo()
            self.flight_stop_info = temp_model.from_map(m.get('flight_stop_info'))

        if m.get('flight_transfer_info') is not None:
            temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListFlightTransferInfo()
            self.flight_transfer_info = temp_model.from_map(m.get('flight_transfer_info'))

        if m.get('flight_type') is not None:
            self.flight_type = m.get('flight_type')

        if m.get('journey_seq') is not None:
            self.journey_seq = m.get('journey_seq')

        if m.get('left_num') is not None:
            self.left_num = m.get('left_num')

        if m.get('manufacturer') is not None:
            self.manufacturer = m.get('manufacturer')

        if m.get('meal_desc') is not None:
            self.meal_desc = m.get('meal_desc')

        if m.get('price_info_d_t_o') is not None:
            temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListPriceInfoDTO()
            self.price_info_dto = temp_model.from_map(m.get('price_info_d_t_o'))

        if m.get('segment_seq') is not None:
            self.segment_seq = m.get('segment_seq')

        if m.get('share') is not None:
            self.share = m.get('share')

        if m.get('short_flight_size') is not None:
            self.short_flight_size = m.get('short_flight_size')

        if m.get('span_day') is not None:
            self.span_day = m.get('span_day')

        if m.get('stop') is not None:
            self.stop = m.get('stop')

        if m.get('transfer') is not None:
            self.transfer = m.get('transfer')

        return self

class FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListPriceInfoDTO(DaraModel):
    def __init__(
        self,
        adult_price: int = None,
        adult_tax: int = None,
        adult_total_price: int = None,
        before_control_price: int = None,
        child_price: int = None,
        child_tax: int = None,
        child_total_price: int = None,
        infant_price: int = None,
        infant_tax: int = None,
        infant_total_price: int = None,
        original_adult_price: int = None,
        original_adult_total_price: int = None,
        re_shop_price_info_dto: main_models.FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListPriceInfoDTOReShopPriceInfoDTO = None,
    ):
        self.adult_price = adult_price
        self.adult_tax = adult_tax
        self.adult_total_price = adult_total_price
        self.before_control_price = before_control_price
        self.child_price = child_price
        self.child_tax = child_tax
        self.child_total_price = child_total_price
        self.infant_price = infant_price
        self.infant_tax = infant_tax
        self.infant_total_price = infant_total_price
        self.original_adult_price = original_adult_price
        self.original_adult_total_price = original_adult_total_price
        self.re_shop_price_info_dto = re_shop_price_info_dto

    def validate(self):
        if self.re_shop_price_info_dto:
            self.re_shop_price_info_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adult_price is not None:
            result['adult_price'] = self.adult_price

        if self.adult_tax is not None:
            result['adult_tax'] = self.adult_tax

        if self.adult_total_price is not None:
            result['adult_total_price'] = self.adult_total_price

        if self.before_control_price is not None:
            result['before_control_price'] = self.before_control_price

        if self.child_price is not None:
            result['child_price'] = self.child_price

        if self.child_tax is not None:
            result['child_tax'] = self.child_tax

        if self.child_total_price is not None:
            result['child_total_price'] = self.child_total_price

        if self.infant_price is not None:
            result['infant_price'] = self.infant_price

        if self.infant_tax is not None:
            result['infant_tax'] = self.infant_tax

        if self.infant_total_price is not None:
            result['infant_total_price'] = self.infant_total_price

        if self.original_adult_price is not None:
            result['original_adult_price'] = self.original_adult_price

        if self.original_adult_total_price is not None:
            result['original_adult_total_price'] = self.original_adult_total_price

        if self.re_shop_price_info_dto is not None:
            result['re_shop_price_info_d_t_o'] = self.re_shop_price_info_dto.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adult_price') is not None:
            self.adult_price = m.get('adult_price')

        if m.get('adult_tax') is not None:
            self.adult_tax = m.get('adult_tax')

        if m.get('adult_total_price') is not None:
            self.adult_total_price = m.get('adult_total_price')

        if m.get('before_control_price') is not None:
            self.before_control_price = m.get('before_control_price')

        if m.get('child_price') is not None:
            self.child_price = m.get('child_price')

        if m.get('child_tax') is not None:
            self.child_tax = m.get('child_tax')

        if m.get('child_total_price') is not None:
            self.child_total_price = m.get('child_total_price')

        if m.get('infant_price') is not None:
            self.infant_price = m.get('infant_price')

        if m.get('infant_tax') is not None:
            self.infant_tax = m.get('infant_tax')

        if m.get('infant_total_price') is not None:
            self.infant_total_price = m.get('infant_total_price')

        if m.get('original_adult_price') is not None:
            self.original_adult_price = m.get('original_adult_price')

        if m.get('original_adult_total_price') is not None:
            self.original_adult_total_price = m.get('original_adult_total_price')

        if m.get('re_shop_price_info_d_t_o') is not None:
            temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListPriceInfoDTOReShopPriceInfoDTO()
            self.re_shop_price_info_dto = temp_model.from_map(m.get('re_shop_price_info_d_t_o'))

        return self

class FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListPriceInfoDTOReShopPriceInfoDTO(DaraModel):
    def __init__(
        self,
        re_shop_adult_change_fee: int = None,
        re_shop_adult_price: int = None,
        re_shop_adult_price_gap: int = None,
        re_shop_child_change_fee: int = None,
        re_shop_child_price: int = None,
        re_shop_child_price_gap: int = None,
        re_shop_inf_change_fee: int = None,
        re_shop_inf_price: int = None,
        re_shop_inf_price_gap: int = None,
    ):
        self.re_shop_adult_change_fee = re_shop_adult_change_fee
        self.re_shop_adult_price = re_shop_adult_price
        self.re_shop_adult_price_gap = re_shop_adult_price_gap
        self.re_shop_child_change_fee = re_shop_child_change_fee
        self.re_shop_child_price = re_shop_child_price
        self.re_shop_child_price_gap = re_shop_child_price_gap
        self.re_shop_inf_change_fee = re_shop_inf_change_fee
        self.re_shop_inf_price = re_shop_inf_price
        self.re_shop_inf_price_gap = re_shop_inf_price_gap

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.re_shop_adult_change_fee is not None:
            result['re_shop_adult_change_fee'] = self.re_shop_adult_change_fee

        if self.re_shop_adult_price is not None:
            result['re_shop_adult_price'] = self.re_shop_adult_price

        if self.re_shop_adult_price_gap is not None:
            result['re_shop_adult_price_gap'] = self.re_shop_adult_price_gap

        if self.re_shop_child_change_fee is not None:
            result['re_shop_child_change_fee'] = self.re_shop_child_change_fee

        if self.re_shop_child_price is not None:
            result['re_shop_child_price'] = self.re_shop_child_price

        if self.re_shop_child_price_gap is not None:
            result['re_shop_child_price_gap'] = self.re_shop_child_price_gap

        if self.re_shop_inf_change_fee is not None:
            result['re_shop_inf_change_fee'] = self.re_shop_inf_change_fee

        if self.re_shop_inf_price is not None:
            result['re_shop_inf_price'] = self.re_shop_inf_price

        if self.re_shop_inf_price_gap is not None:
            result['re_shop_inf_price_gap'] = self.re_shop_inf_price_gap

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('re_shop_adult_change_fee') is not None:
            self.re_shop_adult_change_fee = m.get('re_shop_adult_change_fee')

        if m.get('re_shop_adult_price') is not None:
            self.re_shop_adult_price = m.get('re_shop_adult_price')

        if m.get('re_shop_adult_price_gap') is not None:
            self.re_shop_adult_price_gap = m.get('re_shop_adult_price_gap')

        if m.get('re_shop_child_change_fee') is not None:
            self.re_shop_child_change_fee = m.get('re_shop_child_change_fee')

        if m.get('re_shop_child_price') is not None:
            self.re_shop_child_price = m.get('re_shop_child_price')

        if m.get('re_shop_child_price_gap') is not None:
            self.re_shop_child_price_gap = m.get('re_shop_child_price_gap')

        if m.get('re_shop_inf_change_fee') is not None:
            self.re_shop_inf_change_fee = m.get('re_shop_inf_change_fee')

        if m.get('re_shop_inf_price') is not None:
            self.re_shop_inf_price = m.get('re_shop_inf_price')

        if m.get('re_shop_inf_price_gap') is not None:
            self.re_shop_inf_price_gap = m.get('re_shop_inf_price_gap')

        return self

class FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListFlightTransferInfo(DaraModel):
    def __init__(
        self,
        transfer_airline_info: main_models.FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListFlightTransferInfoTransferAirlineInfo = None,
        transfer_city_code: str = None,
        transfer_city_name: str = None,
        transfer_dep_time: str = None,
        transfer_flight_no: str = None,
        transfer_flight_size: str = None,
        transfer_share: bool = None,
        transfer_stop_time: int = None,
    ):
        self.transfer_airline_info = transfer_airline_info
        self.transfer_city_code = transfer_city_code
        self.transfer_city_name = transfer_city_name
        self.transfer_dep_time = transfer_dep_time
        self.transfer_flight_no = transfer_flight_no
        self.transfer_flight_size = transfer_flight_size
        self.transfer_share = transfer_share
        self.transfer_stop_time = transfer_stop_time

    def validate(self):
        if self.transfer_airline_info:
            self.transfer_airline_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.transfer_airline_info is not None:
            result['transfer_airline_info'] = self.transfer_airline_info.to_map()

        if self.transfer_city_code is not None:
            result['transfer_city_code'] = self.transfer_city_code

        if self.transfer_city_name is not None:
            result['transfer_city_name'] = self.transfer_city_name

        if self.transfer_dep_time is not None:
            result['transfer_dep_time'] = self.transfer_dep_time

        if self.transfer_flight_no is not None:
            result['transfer_flight_no'] = self.transfer_flight_no

        if self.transfer_flight_size is not None:
            result['transfer_flight_size'] = self.transfer_flight_size

        if self.transfer_share is not None:
            result['transfer_share'] = self.transfer_share

        if self.transfer_stop_time is not None:
            result['transfer_stop_time'] = self.transfer_stop_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('transfer_airline_info') is not None:
            temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListFlightTransferInfoTransferAirlineInfo()
            self.transfer_airline_info = temp_model.from_map(m.get('transfer_airline_info'))

        if m.get('transfer_city_code') is not None:
            self.transfer_city_code = m.get('transfer_city_code')

        if m.get('transfer_city_name') is not None:
            self.transfer_city_name = m.get('transfer_city_name')

        if m.get('transfer_dep_time') is not None:
            self.transfer_dep_time = m.get('transfer_dep_time')

        if m.get('transfer_flight_no') is not None:
            self.transfer_flight_no = m.get('transfer_flight_no')

        if m.get('transfer_flight_size') is not None:
            self.transfer_flight_size = m.get('transfer_flight_size')

        if m.get('transfer_share') is not None:
            self.transfer_share = m.get('transfer_share')

        if m.get('transfer_stop_time') is not None:
            self.transfer_stop_time = m.get('transfer_stop_time')

        return self

class FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListFlightTransferInfoTransferAirlineInfo(DaraModel):
    def __init__(
        self,
        airline_chinese_name: str = None,
        airline_chinese_short_name: str = None,
        airline_code: str = None,
        airline_icon: str = None,
        cheap_flight: bool = None,
    ):
        self.airline_chinese_name = airline_chinese_name
        self.airline_chinese_short_name = airline_chinese_short_name
        self.airline_code = airline_code
        self.airline_icon = airline_icon
        self.cheap_flight = cheap_flight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_chinese_name is not None:
            result['airline_chinese_name'] = self.airline_chinese_name

        if self.airline_chinese_short_name is not None:
            result['airline_chinese_short_name'] = self.airline_chinese_short_name

        if self.airline_code is not None:
            result['airline_code'] = self.airline_code

        if self.airline_icon is not None:
            result['airline_icon'] = self.airline_icon

        if self.cheap_flight is not None:
            result['cheap_flight'] = self.cheap_flight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_chinese_name') is not None:
            self.airline_chinese_name = m.get('airline_chinese_name')

        if m.get('airline_chinese_short_name') is not None:
            self.airline_chinese_short_name = m.get('airline_chinese_short_name')

        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_icon') is not None:
            self.airline_icon = m.get('airline_icon')

        if m.get('cheap_flight') is not None:
            self.cheap_flight = m.get('cheap_flight')

        return self

class FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListFlightStopInfo(DaraModel):
    def __init__(
        self,
        stop_airport: str = None,
        stop_arr_term: str = None,
        stop_arr_time: str = None,
        stop_city_code: str = None,
        stop_city_name: str = None,
        stop_dep_term: str = None,
        stop_dep_time: str = None,
    ):
        self.stop_airport = stop_airport
        self.stop_arr_term = stop_arr_term
        self.stop_arr_time = stop_arr_time
        self.stop_city_code = stop_city_code
        self.stop_city_name = stop_city_name
        self.stop_dep_term = stop_dep_term
        self.stop_dep_time = stop_dep_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stop_airport is not None:
            result['stop_airport'] = self.stop_airport

        if self.stop_arr_term is not None:
            result['stop_arr_term'] = self.stop_arr_term

        if self.stop_arr_time is not None:
            result['stop_arr_time'] = self.stop_arr_time

        if self.stop_city_code is not None:
            result['stop_city_code'] = self.stop_city_code

        if self.stop_city_name is not None:
            result['stop_city_name'] = self.stop_city_name

        if self.stop_dep_term is not None:
            result['stop_dep_term'] = self.stop_dep_term

        if self.stop_dep_time is not None:
            result['stop_dep_time'] = self.stop_dep_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stop_airport') is not None:
            self.stop_airport = m.get('stop_airport')

        if m.get('stop_arr_term') is not None:
            self.stop_arr_term = m.get('stop_arr_term')

        if m.get('stop_arr_time') is not None:
            self.stop_arr_time = m.get('stop_arr_time')

        if m.get('stop_city_code') is not None:
            self.stop_city_code = m.get('stop_city_code')

        if m.get('stop_city_name') is not None:
            self.stop_city_name = m.get('stop_city_name')

        if m.get('stop_dep_term') is not None:
            self.stop_dep_term = m.get('stop_dep_term')

        if m.get('stop_dep_time') is not None:
            self.stop_dep_time = m.get('stop_dep_time')

        return self

class FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListFlightShareInfo(DaraModel):
    def __init__(
        self,
        operating_airline_info: main_models.FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListFlightShareInfoOperatingAirlineInfo = None,
        operating_flight_no: str = None,
    ):
        self.operating_airline_info = operating_airline_info
        self.operating_flight_no = operating_flight_no

    def validate(self):
        if self.operating_airline_info:
            self.operating_airline_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operating_airline_info is not None:
            result['operating_airline_info'] = self.operating_airline_info.to_map()

        if self.operating_flight_no is not None:
            result['operating_flight_no'] = self.operating_flight_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operating_airline_info') is not None:
            temp_model = main_models.FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListFlightShareInfoOperatingAirlineInfo()
            self.operating_airline_info = temp_model.from_map(m.get('operating_airline_info'))

        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')

        return self

class FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListFlightShareInfoOperatingAirlineInfo(DaraModel):
    def __init__(
        self,
        airline_chinese_name: str = None,
        airline_chinese_short_name: str = None,
        airline_code: str = None,
        airline_icon: str = None,
        cheap_flight: bool = None,
    ):
        self.airline_chinese_name = airline_chinese_name
        self.airline_chinese_short_name = airline_chinese_short_name
        self.airline_code = airline_code
        self.airline_icon = airline_icon
        self.cheap_flight = cheap_flight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_chinese_name is not None:
            result['airline_chinese_name'] = self.airline_chinese_name

        if self.airline_chinese_short_name is not None:
            result['airline_chinese_short_name'] = self.airline_chinese_short_name

        if self.airline_code is not None:
            result['airline_code'] = self.airline_code

        if self.airline_icon is not None:
            result['airline_icon'] = self.airline_icon

        if self.cheap_flight is not None:
            result['cheap_flight'] = self.cheap_flight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_chinese_name') is not None:
            self.airline_chinese_name = m.get('airline_chinese_name')

        if m.get('airline_chinese_short_name') is not None:
            self.airline_chinese_short_name = m.get('airline_chinese_short_name')

        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_icon') is not None:
            self.airline_icon = m.get('airline_icon')

        if m.get('cheap_flight') is not None:
            self.cheap_flight = m.get('cheap_flight')

        return self

class FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListDepAirportInfo(DaraModel):
    def __init__(
        self,
        airport_code: str = None,
        airport_name: str = None,
        airport_short_name: str = None,
        terminal: str = None,
    ):
        self.airport_code = airport_code
        self.airport_name = airport_name
        self.airport_short_name = airport_short_name
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

        if self.airport_short_name is not None:
            result['airport_short_name'] = self.airport_short_name

        if self.terminal is not None:
            result['terminal'] = self.terminal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airport_code') is not None:
            self.airport_code = m.get('airport_code')

        if m.get('airport_name') is not None:
            self.airport_name = m.get('airport_name')

        if m.get('airport_short_name') is not None:
            self.airport_short_name = m.get('airport_short_name')

        if m.get('terminal') is not None:
            self.terminal = m.get('terminal')

        return self

class FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListArrAirportInfo(DaraModel):
    def __init__(
        self,
        airport_code: str = None,
        airport_name: str = None,
        airport_short_name: str = None,
        terminal: str = None,
    ):
        self.airport_code = airport_code
        self.airport_name = airport_name
        self.airport_short_name = airport_short_name
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

        if self.airport_short_name is not None:
            result['airport_short_name'] = self.airport_short_name

        if self.terminal is not None:
            result['terminal'] = self.terminal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airport_code') is not None:
            self.airport_code = m.get('airport_code')

        if m.get('airport_name') is not None:
            self.airport_name = m.get('airport_name')

        if m.get('airport_short_name') is not None:
            self.airport_short_name = m.get('airport_short_name')

        if m.get('terminal') is not None:
            self.terminal = m.get('terminal')

        return self

class FlightModifyListingSearchV2ResponseBodyModuleDirectFlightListAirlineInfo(DaraModel):
    def __init__(
        self,
        airline_chinese_name: str = None,
        airline_chinese_short_name: str = None,
        airline_code: str = None,
        airline_icon: str = None,
        cheap_flight: bool = None,
    ):
        self.airline_chinese_name = airline_chinese_name
        self.airline_chinese_short_name = airline_chinese_short_name
        self.airline_code = airline_code
        self.airline_icon = airline_icon
        self.cheap_flight = cheap_flight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_chinese_name is not None:
            result['airline_chinese_name'] = self.airline_chinese_name

        if self.airline_chinese_short_name is not None:
            result['airline_chinese_short_name'] = self.airline_chinese_short_name

        if self.airline_code is not None:
            result['airline_code'] = self.airline_code

        if self.airline_icon is not None:
            result['airline_icon'] = self.airline_icon

        if self.cheap_flight is not None:
            result['cheap_flight'] = self.cheap_flight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_chinese_name') is not None:
            self.airline_chinese_name = m.get('airline_chinese_name')

        if m.get('airline_chinese_short_name') is not None:
            self.airline_chinese_short_name = m.get('airline_chinese_short_name')

        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_icon') is not None:
            self.airline_icon = m.get('airline_icon')

        if m.get('cheap_flight') is not None:
            self.cheap_flight = m.get('cheap_flight')

        return self

